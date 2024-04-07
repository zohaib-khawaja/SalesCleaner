import pandas as pd

def ingest_json(file_path):
    data = pd.read_json(file_path)
    return data