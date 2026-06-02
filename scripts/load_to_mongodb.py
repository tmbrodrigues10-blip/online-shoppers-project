import pandas as pd
from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017/"
)

db = client["online_shoppers"]

collection = db["customers"]

df = pd.read_csv(
    "cleaned/online-shoppers-clean.csv"
)

records = df.to_dict("records")

collection.insert_many(records)

print("Dados inseridos")