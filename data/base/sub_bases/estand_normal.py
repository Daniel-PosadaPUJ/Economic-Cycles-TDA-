import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# === 1. Cargar datos ===
df = pd.read_csv("base_macro_filtrada.csv")

# === 2. Identificar columnas numéricas (excepto fecha) ===
num_cols = [c for c in df.columns if c.lower() != "fecha"]

# === 3. Limpieza: quitar % y reemplazar comas por puntos ===
for col in num_cols:
    df[col] = (
        df[col]
        .astype(str)                 # asegurar que todo sea string
        .str.replace("%", "", regex=False)  # quitar %
        .str.replace(",", ".", regex=False) # cambiar coma a punto
    )
    df[col] = pd.to_numeric(df[col], errors="coerce")  # convertir a float

# === 4. Escaladores ===
scaler_std = StandardScaler()
scaler_minmax = MinMaxScaler()

df_std = pd.DataFrame(
    scaler_std.fit_transform(df[num_cols]),
    columns=num_cols,
    index=df.index
)

df_minmax = pd.DataFrame(
    scaler_minmax.fit_transform(df[num_cols]),
    columns=num_cols,
    index=df.index
)


df_std.to_csv("macro_base_scaled.csv", index=False, encoding="utf-8")
df_minmax.to_csv("macro_base_normalize.csv", index=False, encoding="utf-8")

