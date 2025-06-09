import streamlit as st
from docx import Document
import pdfplumber

def load_comments(file):
    data=[]
    if file.type.endswith("document"):
        doc = Document(file)
        for p in doc.paragraphs:
            if ":" in p.text:
                data.append(p.text.strip())
    else:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                for line in page.extract_text().split("\n"):
                    if ":" in line:
                        data.append(line.strip())
    return data

def show_comments(comments, student):
    if not comments:
        st.info("Нет комментариев.")
    for c in comments:
        st.write(f"- {c}")
