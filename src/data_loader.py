import pandas as pd
import streamlit as st

def load_main_data(uploaded_file):
    df = pd.read_excel(uploaded_file, sheet_name="Ввод данных", engine="openpyxl")
    df["Дата"] = pd.to_datetime(df["Дата"], errors="coerce")
    dropped = df["Дата"].isna().sum()
    if dropped:
        st.warning(f"Отброшено {dropped} строк(и) с некорректной датой")
    return df.dropna(subset=["Дата"])
