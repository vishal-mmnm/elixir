import streamlit as st
import requests

# Heading block
st.title("Your Streamlit App")

# Description block
st.markdown("""
This is a simple Streamlit app that takes user input and makes an API call when a button is clicked.
""")

# Text input
rfla = st.text_input("Please entre PDB identifier(s) space delimited:")

# Button
if st.button('Call API'):
    # Make the API call
    # NOTE: Replace 'http://api.example.com' with your actual API endpoint
    response = requests.get(f'http://35.194.49.193/pdbrenum?rfla={rfla}h&mmCIF=true', stream=True)
    # response contains file
    # download file

    file_data = b""
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:  # filter out keep-alive new chunks
            file_data += chunk

    # Provide a download button for the file
    st.download_button(
        label="Download the file",
        data=file_data,
        file_name="response.zip",
        mime="application/zip"
    )
