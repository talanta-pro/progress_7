import streamlit as st
from src.data_loader import load_main_data
from src.charts import plot_grades
from src.comments import show_comments, load_comments
from src.portraits import show_portrait
from src.export_utils import export_report

st.set_page_config(page_title="Анализ прогресса учеников", layout="wide")
st.title("Анализ прогресса учеников")

# Sidebar uploads
data_file = st.sidebar.file_uploader("Excel-файл (лист 'Ввод данных')", type="xlsx")
comment_file = st.sidebar.file_uploader("Комментарии (.docx/.pdf)", type=["docx","pdf"])
portrait_files = st.sidebar.file_uploader("Портреты (.docx/.pdf)", type=["docx","pdf"], accept_multiple_files=True)

if not data_file:
    st.info("Загрузите Excel-файл с данными.")
    st.stop()

df = load_main_data(data_file)
students = df["ФИО ученика"].unique().tolist()
student = st.selectbox("Выберите ученика", students)

tabs = st.tabs(["Графики", "Комментарии", "Портреты", "Экспорт"])
with tabs[0]:
    subject = st.selectbox("Предмет (или Все)", ["Все"] + df["Предмет"].unique().tolist())
    if subject=="Все":
        subject=None
    plot_grades(df, student, subject)
with tabs[1]:
    if comment_file:
        comments = load_comments(comment_file)
        show_comments(comments, student)
    else:
        st.info("Загрузите файл с комментариями.")
with tabs[2]:
    show_portrait(portrait_files or [], student)
with tabs[3]:
    export_report(df, student)
