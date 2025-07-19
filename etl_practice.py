# etl_practice.py

import pandas as pd
import xml.etree.ElementTree as ET
import glob
from datetime import datetime

def log(message):
    with open("log_file.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - {message}\n")

def extract_from_csv(file_path):
    return pd.read_csv(file_path)

def extract_from_json(file_path):
    return pd.read_json(file_path, lines=True)

def extract_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []
    for car in root:
        car_data = {}
        for element in car:
            car_data[element.tag] = element.text
        data.append(car_data)
    return pd.DataFrame(data)

def extract_all():
    log("Start extraction")

    csv_df1 = extract_from_csv("used_car_prices1.csv")
    csv_df2 = extract_from_csv("used_car_prices2.csv")
    csv_df3 = extract_from_csv("used_car_prices3.csv")

    json_df1 = extract_from_json("used_car_prices1.json")
    json_df2 = extract_from_json("used_car_prices2.json")
    json_df3 = extract_from_json("used_car_prices3.json")

    xml_df1 = extract_from_xml("used_car_prices1.xml")
    xml_df2 = extract_from_xml("used_car_prices2.xml")
    xml_df3 = extract_from_xml("used_car_prices3.xml")

    df = pd.concat([
        csv_df1, csv_df2, csv_df3,
        json_df1, json_df2, json_df3,
        xml_df1, xml_df2, xml_df3
    ], ignore_index=True)

    log("Extraction completed")
    return df

def transform(df):
    log("Start transformation")
    df["price"] = df["price"].astype(float).round(2)
    log("Transformation completed")
    return df

def load(df):
    df.to_csv("transformed_data.csv", index=False)
    log("Data loaded to transformed_data.csv")

def etl_process():
    df = extract_all()
    df = transform(df)
    load(df)

etl_process()