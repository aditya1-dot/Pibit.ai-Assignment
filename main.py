import streamlit as st
import json
import os
import tempfile
from utils import parse_pdf, parse_docx, get_file_extension

def parse_resume(file_path, file_extension):
    """
    Parse a resume file (PDF or DOCX) and return JSON format.
    """
    if file_extension == ".pdf":
        text = parse_pdf(file_path)
    elif file_extension == ".docx":
        text = parse_docx(file_path)
    else:
        st.error("Unsupported file format. Please upload a PDF or DOCX file.")
        return None

    # Convert text to JSON format
    parsed_data = {"content": text}
    return json.dumps(parsed_data, indent=4)

def main():
    st.title("Resume Parser")

    uploaded_file = st.file_uploader("Upload a resume (PDF or DOCX)", type=["pdf", "docx"])

    if uploaded_file is not None:
        # st.markdown("### Uploaded Resume:")
        # st.text(uploaded_file.name)

        file_extension = get_file_extension(uploaded_file.name)

        with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name

        # st.markdown("### Parsed Content:")
        # if st.button("Parse"):
        result = parse_resume(tmp_file_path, file_extension)
        if result:
                st.json(result)

        # Clean up temporary file
        os.remove(tmp_file_path)

if __name__ == "__main__":
    main()
