import pandas as pd

def ingest_excel(file_path):
    data = pd.read_excel(file_path)
    return data