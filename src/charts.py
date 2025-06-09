import altair as alt
import streamlit as st

def plot_grades(df, student, subject=None):
    sub = df[df["ФИО ученика"]==student]
    if subject:
        sub = sub[sub["Предмет"]==subject]
    if sub.empty:
        st.info("Нет данных.")
        return
    chart = alt.Chart(sub).mark_line(point=True).encode(
        x="Дата:T", y="Оценка (1-5):Q", color="Предмет:N",
        tooltip=["Дата","Предмет","Оценка (1-5)"]
    ).interactive()
    st.altair_chart(chart, use_container_width=True)
