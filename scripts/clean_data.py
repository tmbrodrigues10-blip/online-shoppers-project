import pandas as pd
import numpy as np

# 1. Carregar dataset
df = pd.read_csv("raw/online-shoppers-dirty.csv", sep=";")

# 2. Limpar nomes das colunas
df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

# 3. Remover coluna de índice desnecessária
if "Unnamed:_0" in df.columns:
    df.drop(columns=["Unnamed:_0"], inplace=True)

# 4. Remover espaços extras em colunas de texto
for col in df.select_dtypes(include=["object", "string"]):
    df[col] = df[col].str.strip()

# 5. Corrigir valores em falta e inválidos
df.replace(["?", "unknown"], np.nan, inplace=True)

# 6. Uniformizar a coluna Month
month_map = {
    "02": "Feb",
    "feb": "Feb",
    "FEB": "Feb",
    "05": "May",
    "may": "May",
    "MAY": "May",
    "11": "Nov",
    "nov": "Nov",
    "June": "Jun"
}

df["Month"] = df["Month"].replace(month_map)

# 7. Uniformizar VisitorType
visitor_map = {
    "RETURNING": "Returning_Visitor",
    "Returning Visitor": "Returning_Visitor",
    "NEW": "New_Visitor",
    "New Visitor": "New_Visitor"
}

df["VisitorType"] = df["VisitorType"].replace(visitor_map)

# 8. Converter colunas numéricas
numeric_cols = [
    "Administrative",
    "Administrative_Duration",
    "ProductRelated_Duration",
    "Bouncerates",
    "PageValues"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 9. Preencher valores em falta
for col in df.columns:

    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].median())

    else:
        moda = df[col].mode()
        if not moda.empty:
            df[col] = df[col].fillna(moda[0])
# 10. Verificar resultado
print("\nValores em falta por coluna:")
print(df.isnull().sum())

print("\nNúmero de linhas duplicadas:")
print(df.duplicated().sum())

# 11. Guardar dataset limpo
df.to_csv("online-shoppers-clean.csv", index=False)

print("\nDataset limpo guardado em 'online-shoppers-clean.csv'")