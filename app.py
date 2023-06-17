import streamlit as st
import requests

# Heading block
st.title("PDBrenum")

# Description block
st.markdown("""
PDBrenum provides PDB files in mmCIF and legacy-PDB format in which residues in the coordinates (and all other fields) are renumbered according to their UniProt sequences.
""")
            
col1, col2 = st.columns(2)

options = ['mmCIF', 'PDB']

with col1:
    # Text input
    rfla = st.text_input("Please entre PDB identifier(s) space delimited:")

with col2:
    options = ['mmCIF', 'PDB']
    selected_option = st.selectbox("Select PDB Format", options)

# Button
if st.button('Generate Renumebred PDB'):
    with st.spinner('This will take a couple of seconds...'):

        # Make the API call
        # NOTE: Replace 'http://api.example.com' with your actual API endpoint
        response = requests.get(f'http://35.194.49.193/pdbrenum?rfla={rfla}&mmCIF={"true" if selected_option == "mmCIF" else "false"}&PDB={"true" if selected_option == "PDB" else "false"}', stream=True)
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
