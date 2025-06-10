import streamlit as st
import altair as alt

def show(df):
    st.subheader("Ошибки")
    if "Ошибка" not in df.columns:
        st.warning("Нет колонки 'Ошибка'")
        return
    grp = df.groupby("Ошибка").size().reset_index(name="Count")
    chart = alt.Chart(grp).mark_bar().encode(
        x="Count:Q", y="Ошибка:N"
    )
    st.altair_chart(chart, use_container_width=True)