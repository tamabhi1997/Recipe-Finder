Recipe-Finder
  🍳 Recipe Finder is a web application that allows users to search for recipes based on recipe names or ingredients. This app is built using   Streamlit for the frontend and Flask with Elasticsearch for the backend, providing a seamless and fast search experience.

Features
   - Search recipes by name or ingredients.
   - Display detailed information about each recipe:
     - Ingredients
     - Directions
     - Source links
     - Tags
  Constant recipe image for a consistent user experience.
  Fast and scalable search using Elasticsearch.


 - Requirements
  - Backend
    - Python 3.8+
    - Elasticsearch 8.x
    - Flask
    - Required Python packages:
      - pip install flask elasticsearch requests
  - Frontend
    - Streamlit
    - Required Python packages:
    - pip install streamlit pandas requests


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

Screenshots:-
<img width="1470" alt="Screenshot 2024-11-27 at 4 08 01 PM" src="https://github.com/user-attachments/assets/2ce8f48d-b407-4197-b48f-3ed77a3b1093">

<img width="1470" alt="Screenshot 2024-11-27 at 4 08 12 PM" src="https://github.com/user-attachments/assets/56d3f2d2-4492-463b-9add-4c026bc316d9">


Credits
  Recipe Dataset: [RecipeNLG Dataset](url)

