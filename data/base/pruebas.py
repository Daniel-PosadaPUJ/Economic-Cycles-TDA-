import pandas as pd

# Leer TRM original
df = pd.read_csv("Tasa_de_Cambio_Representativa_del_Mercado-_TRM_20250824.csv")

print(df.head())

# Convertir fechas
df["VIGENCIADESDE"] = pd.to_datetime(df["VIGENCIADESDE"], dayfirst=True)
df["VIGENCIAHASTA"] = pd.to_datetime(df["VIGENCIAHASTA"], dayfirst=True)

# Expandir a un rango de meses en lugar de días
rows = []
for _, row in df.iterrows():
    meses = pd.period_range(row["VIGENCIADESDE"], row["VIGENCIAHASTA"], freq="M")
    for m in meses:
        rows.append({"Periodo": m.strftime("%Y-%m"),
                     "TRM": float(str(row["VALOR"]).replace("$", "").replace(",", ""))})

df_monthly = pd.DataFrame(rows)

# Tomar mediana por mes (en caso de repeticiones)
df_monthly = df_monthly.groupby("Periodo", as_index=False)["TRM"].median()

# Ajustar rango (2003-01 a 2025-01)
all_months = pd.period_range("2003-01", "2025-01", freq="M").strftime("%Y-%m")
df_monthly = df_monthly.set_index("Periodo").reindex(all_months).ffill().reset_index()
df_monthly.columns = ["Periodo", "TRM"]

# Guardar
df_monthly.to_csv("trm_mensual.csv", index=False)

print(df_monthly.head(), df_monthly.tail())

