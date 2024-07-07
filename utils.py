import fitz  # PyMuPDF for PDF parsing
from docx import Document  # python-docx for Word document parsing
import re
import os

def parse_pdf(filepath):
    """
    Parse a PDF file and return a structured dictionary of headings and their content.
    """
    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return structure_text(text)

def parse_docx(filepath):
    """
    Parse a Word document (.docx) and return a structured dictionary of headings and their content.
    """
    doc = Document(filepath)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return structure_text(text)

def get_file_extension(filename):
    """
    Get the file extension from a filename.
    """
    return os.path.splitext(filename)[1]

def structure_text(text):
    """
    Structure the parsed text into headings and their content.
    """
    # Define a regex pattern to identify headings (adjust based on common heading formats)
    heading_pattern = re.compile(r'\n\s*(?:[A-Z][A-Za-z\s]*)\s*\n')
    sections = re.split(heading_pattern, text)
    headings = heading_pattern.findall(text)

    # Clean up headings and sections
    headings = [heading.strip() for heading in headings]
    sections = [section.strip() for section in sections]

    # Combine headings and sections into a dictionary
    structured_data = {}
    for i, heading in enumerate(headings):
        if i < len(sections):
            structured_data[heading] = sections[i+1] if i+1 < len(sections) else ''

    return structured_data
