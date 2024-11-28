import json
import streamlit as st
import pandas as pd
import requests

# Set up the Streamlit app
st.set_page_config(page_title="🍳 Recipe Finder", layout="wide")
st.title("🍳 Recipe Finder")

# Add a subtitle and description
st.markdown(
    """
    ### Explore delicious recipes!
    Search for recipes by name or ingredients, and get inspired to create your next meal.
    """
)

# Backend API URL
BACKEND_URL = "http://127.0.0.1:5000/search"

# Create a sidebar for filters or additional options
st.sidebar.header("Search Options")
query = st.sidebar.text_input("Enter recipe name or ingredients (e.g., 'chicken, rice'):").strip()

# Add an image or GIF to make it more appealing
st.sidebar.image(
    "https://media.giphy.com/media/l0MYC0LajbaPoEADu/giphy.gif",
    caption="What's cooking?",
    use_column_width=True,
)

# Add a search button in the sidebar
if st.sidebar.button("Search Recipes"):
    if not query:
        st.warning("Please enter a recipe name or ingredients to search.")
    else:
        # Call the backend API
        with st.spinner("Searching for recipes..."):
            try:
                params = {"q": query}
                response = requests.get(BACKEND_URL, params=params)

                if response.status_code == 200:
                    results = response.json()
                    if results:
                        st.success(f"Found {len(results)} matching recipe(s):")

                        # Display results in a grid
                        for result in results:
                            with st.container():
                                st.subheader(result["recipe_name"])
                                cols = st.columns([1, 3])
                                with cols[0]:
                                    st.image(
                                        "https://https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.gettyimages.com%2Fphotos%2Fpreparing-food&psig=AOvVaw1iZYcOiEEs9LXeoykwZj6g&ust=1732762903632000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCMCQoIbD-4kDFQAAAAAdAAAAABAE/150",  # Placeholder for recipe image
                                        caption="Recipe Image",
                                        use_column_width=True,
                                    )
                                with cols[1]:
                                    st.write(f"**Ingredients:**")
                                    st.write(", ".join(result["ingredients"]))
                                    st.write(f"**Directions:**")
                                    for step in result["directions"]:
                                        st.write(f"- {step}")
                                    st.write(f"**Source:** [Link]({result['link']})")
                                    st.write(f"**Tags:** {', '.join(result.get('tags', []))}")
                            st.write("---")
                    else:
                        st.info("No matching recipes found.")
                else:
                    st.error(f"Error {response.status_code}: Unable to fetch results.")
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")

# Add a footer with credits
st.markdown(
    """
    ---
    🥗 Built with [Streamlit](https://streamlit.io) | 💡 Explore recipes and get cooking!
    """
)
