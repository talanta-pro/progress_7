import streamlit as st

def show(df):
    st.subheader("Таблица")
    st.dataframe(df)