import pandas as pd

def load_progress(file):
    df = pd.read_excel(file, sheet_name="Ввод данных", engine="openpyxl")
    df["Дата"] = pd.to_datetime(df["Дата"], errors="coerce")
    return df.dropna(subset=["Дата"])

def load_comments(file):
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file, engine="openpyxl")
    df["Дата"] = pd.to_datetime(df["Дата"], errors="coerce")
    return df.dropna(subset=["Дата"])