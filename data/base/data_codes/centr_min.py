import pandas as pd

# Diccionario de archivos y columnas de interés
datos = {
    "brent_tidy.csv": ["Fecha", "Precio_Brent_USD", "Pct_var_brent"],
    "colcap_tidy.csv": ["Fecha", "Valor_COLCAP", "Pct_var_COLCAP"],
    "ipc_banrep.csv": ["Fecha", "Indice_de_precios_al_Consumidor"],
    "ise_tidy.csv": ["Fecha", "Indicador de Seguimiento a la Economía (ISE)"],
    "ITCR.csv": ["Fecha", "Indice_de_tasa_de_cambio_real"],
    "tasa_desempleo.csv": ["Fecha", "Tasa_de_desempleo_Total_Nacional"],
    "trm_banrep.csv": ["Fecha", "Tasa_de_cambio_promedio_mensual"]
}

# DataFrame central inicializado en None
df_central = None

for archivo, columnas in datos.items():
    # Leer solo las columnas de interés
    df = pd.read_csv(archivo, usecols=columnas)
    
    # Normalizar la columna Fecha
    df["Fecha"] = pd.to_datetime(
        df["Fecha"].astype(str).str.strip(), 
        errors="coerce"
    ).dt.to_period("M")  # solo Año-Mes
    
    # Eliminar fechas inválidas (NaT)
    df = df.dropna(subset=["Fecha"])
    
    # Convertir Periodo a string YYYY-MM
    df["Fecha"] = df["Fecha"].astype(str)
    
    # Merge con el DataFrame central
    if df_central is None:
        df_central = df
    else:
        df_central = pd.merge(df_central, df, on="Fecha", how="inner")

# Ordenar por fecha
df_central = df_central.sort_values("Fecha")

# Guardar el resultado
df_central.to_csv("base_macro_filtrada.csv", index=False, encoding="utf-8")

print("✅ Base de datos unificada creada: base_macro_filtrada.csv")
print("Columnas finales:", df_central.columns.tolist())
print("Rango de fechas:", df_central["Fecha"].min(), "→", df_central["Fecha"].max())

