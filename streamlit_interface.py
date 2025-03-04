import streamlit as st
import requests

# FastAPI URL for matching article
FASTAPI_URL = "http://127.0.0.1:8000/match/"

# Streamlit interface
st.title('Best Article Matching')

# Input field for the user query
user_query = st.text_area('Enter your query:')

if st.button('Find Best Article'):
    if user_query:
        # Make a GET request to FastAPI with the query parameter
        response = requests.get(FASTAPI_URL, params={"query": user_query})

        if response.status_code == 200:
            best_article = response.json()
            st.write(f"Best Article: {best_article['best_match']}")
        else:
            st.write("Error: Could not fetch the best matching article.")
    else:
        st.write("Please enter a query.")
