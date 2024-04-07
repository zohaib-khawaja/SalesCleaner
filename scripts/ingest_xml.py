import xmltodict
import pandas as pd

def ingest_xml(file_path):
    with open(file_path, 'r') as file:
        xml_content = file.read()
    data_dict = xmltodict.parse(xml_content)
    data = pd.json_normalize(data_dict)  # Adjust this based on XML structure
    return data