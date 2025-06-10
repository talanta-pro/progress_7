import streamlit as st

def show(df):
    st.subheader("Комментарии")
    student = st.selectbox("Ученик", df["ФИО ученика"].unique())
    dff = df[df["ФИО ученика"]==student]
    for _, row in dff.iterrows():
        st.write(f"{row['Дата'].date()}: {row.get('Комментарий','')}")