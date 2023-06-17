import streamlit as st
import requests

# Heading block
st.title("PDBrenum")

# Description block
st.markdown("""
PDBrenum provides PDB files in mmCIF and legacy-PDB format in which residues in the coordinates (and all other fields) are renumbered according to their UniProt sequences.
""")

# Text input
rfla = st.text_input("Please entre PDB identifier(s) space delimited:")

# Button
if st.button('Generate Renumebred PDB'):
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
        label="Download the files",
        data=file_data,
        file_name="response.zip",
        mime="application/zip"
    )
