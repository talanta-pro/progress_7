import streamlit as st

def show_portrait(files, student):
    found=False
    for f in files:
        if student in f.name:
            found=True
            st.write(f"### {f.name}")
            st.download_button("Скачать", f.getvalue(), file_name=f.name)
    if not found:
        st.info("Нет портрета для ученика.")
