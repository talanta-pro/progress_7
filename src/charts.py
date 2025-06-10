import streamlit as st
import altair as alt

def show(df):
    st.subheader("Графики")
    student = st.selectbox("Ученик", df["ФИО ученика"].unique())
    dff = df[df["ФИО ученика"]==student]
    chart = alt.Chart(dff).mark_line(point=True).encode(
        x="Дата:T", y="Оценка (1-5):Q", color="Предмет:N",
        tooltip=["Дата","Предмет","Оценка (1-5)"]
    ).interactive()
    st.altair_chart(chart, use_container_width=True)