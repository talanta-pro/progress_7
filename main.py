import streamlit as st
from src.data_loader import load_progress, load_comments
import pages._1_Table as table
import pages._2_Graphics as graphics
import pages._3_Errors as errors
import pages._4_Comments as comments

st.set_page_config(page_title="Анализ прогресса учащихся", layout="wide")
st.title("Анализ прогресса учащихся")

# Sidebar uploads
progress_file = st.sidebar.file_uploader("Excel-файл (Ввод данных)", type="xlsx")
comment_file = st.sidebar.file_uploader("Комментарии (.xlsx/.csv)", type=["xlsx","csv"])

if not progress_file:
    st.warning("Пожалуйста, загрузите файл прогресса.")
    st.stop()

df = load_progress(progress_file)

page = st.sidebar.selectbox("Раздел", ["Table","Graphics","Errors","Comments"])
if page == "Table":
    table.show(df)
elif page == "Graphics":
    graphics.show(df)
elif page == "Errors":
    errors.show(df)
elif page == "Comments":
    if not comment_file:
        st.info("Загрузите файл комментариев.")
    else:
        df_comm = load_comments(comment_file)
        comments.show(df_comm)
