# Recipe-Finder
  🍳 Recipe Finder is a web application that allows users to search for recipes based on recipe names or ingredients. This app is built using   Streamlit for the frontend and Flask with Elasticsearch for the backend, providing a seamless and fast search experience.
------------------------------------------------------------------------------------------------------------------------------------------------
Features
  Search recipes by name or ingredients.
  Display detailed information about each recipe:
    Ingredients
    Directions
    Source links
    Tags
  Constant recipe image for a consistent user experience.
  Fast and scalable search using Elasticsearch.
------------------------------------------------------------------------------------------------------------------------------------------------

Requirements
  Backend
    Python 3.8+
    Elasticsearch 8.x
    Flask
    Required Python packages:
      pip install flask elasticsearch requests
  Frontend
    Streamlit
    Required Python packages:
    pip install streamlit pandas requests

-----------------------------------------------------------------------------------------------------------------------------------------------

How to Run the Project
1. Start Elasticsearch
Ensure Elasticsearch is running locally or on a server. Update the connection details in the backend script if needed.

2. Run the Backend
python backend_app.py
This will start the Flask backend on http://127.0.0.1:5000.

3. Upload Recipe Data
You can upload the recipe dataset using the /upload endpoint in the backend. Use the following curl command:

curl -X POST -F "file=@path_to_your_dataset.json" http://127.0.0.1:5000/upload
Replace path_to_your_dataset.json with the actual path to of the dataset file from the repo.

4. Run the Frontend
Start the Streamlit frontend:

streamlit run frontend_app.py
This will start the app on http://localhost:8501.
