import pandas as pd

# === 1. Cargar las bases ===
macro = pd.read_csv("base_macro_filtrada.csv", index_col=0)
pib = pd.read_csv("pib_mensual_renombrado.csv")

# === 2. Asegurar consistencia en los nombres de columna ===
# (ajusta si la columna de fecha se llama distinto)
if "Fecha" in pib.columns:
    pib["Fecha"] = pd.to_datetime(pib["Fecha"])
    pib.set_index("Fecha", inplace=True)

# === 3. Asegurar que los índices de macro sean tipo fecha ===
macro.index = pd.to_datetime(macro.index)

# === 4. Verificar la columna PIB_PIB en el dataset de PIB ===
if "PIB_PIB" not in pib.columns:
    raise ValueError("La columna 'PIB_PIB' no existe en pib_mensual_renombrado.csv")

# === 5. Hacer merge por fecha (índice) ===
# Se hace una combinación tipo 'left' para mantener las fechas de macro
macro_merged = macro.merge(pib[["PIB_PIB"]], left_index=True, right_index=True, how="left")

# === 6. Verificar valores faltantes o fechas no coincidentes ===
print("Fechas sin PIB_PIB:", macro_merged["PIB_PIB"].isna().sum())

# === 7. Guardar la nueva base ===
macro_merged.to_csv("base_macro_con_pib.csv", encoding="utf-8")

print("✅ Nueva base guardada como 'base_macro_con_pib.csv'")

