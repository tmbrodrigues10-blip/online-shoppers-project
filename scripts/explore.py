import pandas as pd

df = pd.read_csv(
    "raw/online-shoppers-dirty.csv",
    sep=";"
)
print(df.head())
print(df.info())
print(df.isnull().sum())