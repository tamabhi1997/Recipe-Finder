from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch, helpers
import json

app = Flask(__name__)

# Connect to Elasticsearch
es = Elasticsearch("https://localhost:9200", basic_auth=("elastic", "60BYKFcY*t*ltp7A_tCd"), verify_certs=False)

# Index name for recipes
INDEX_NAME = "recipe_name"

if es.ping():
    print("Successfully connected to Elasticsearch!")
else:
    print("Failed to connect to Elasticsearch.")

@app.route('/upload', methods=['POST'])
def upload_data():
    """
    Endpoint to upload recipe data to Elasticsearch.
    Expects a JSON file containing an array of recipes.
    """
    try:
        file = request.files['file']
        data = json.load(file)

        # Prepare bulk upload actions
        actions = [
            {
                "_index": INDEX_NAME,
                "_source": recipe
            }
            for recipe in data
        ]

        # Bulk upload to Elasticsearch
        helpers.bulk(es, actions)
        return jsonify({"message": f"{len(actions)} recipes uploaded successfully."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/search', methods=['GET'])
def search_recipes():
    """
    Endpoint to search recipes by title or ingredients.
    Query Parameters:
      - q: Search query (e.g., 'chicken')
    """
    query = request.args.get('q', '')

    # Construct Elasticsearch query
    # Construct Elasticsearch query
    body = {
        "query": {
            "bool": {
                "should": [
                    {
                        "match": {
                            "recipe_name": {
                                "query": query,
                                "boost": 3  # Higher weight for recipe_name matches
                            }
                        }
                    },
                    {
                        "match": {
                            "ingredients": {
                                "query": query,
                                "boost": 2  # Moderate weight for ingredients matches
                            }
                        }
                    },
                    {
                        "match": {
                            "directions": {
                                "query": query,
                                "boost": 1  # Lowest weight for directions matches
                            }
                        }
                    }
                ],
                "minimum_should_match": 1  # At least one match is required
            }
        }
    }

    try:
        # Perform the search
        res = es.search(index=INDEX_NAME, body=body)
        results = [
            {
                "recipe_name": hit["_source"].get("recipe_name", "Unknown"),
                "ingredients": hit["_source"].get("ingredients", []),
                "directions": hit["_source"].get("directions", []),
                "link": hit["_source"].get("link", "N/A"),
                "tags": hit["_source"].get("tags", [])
            }
            for hit in res['hits']['hits']
        ]
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Check if the index exists; create it if not
    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(index=INDEX_NAME, body={
            "mappings": {
                "properties": {
                    "title": { "type": "text" },
                    "ingredients": { "type": "text" },
                    "directions": { "type": "text" },
                    "link": { "type": "keyword" },
                    "tags": { "type": "text" }
                }
            }
        })
        print(f"Index '{INDEX_NAME}' created successfully.")

    app.run(debug=True)
