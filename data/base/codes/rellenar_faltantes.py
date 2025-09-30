import pandas as pd
import numpy as np

# Leer la base incompleta
df = pd.read_csv("base_central_incompletos.csv", index_col=0, parse_dates=True)

# Identificar tipos de columnas por prefijo
pib_cols = [c for c in df.columns if c.startswith("PIB_")]
ise_cols = [c for c in df.columns if c.startswith("ISE_")]
ipc_cols = [c for c in df.columns if c.startswith("IPC_")]
brent_cols = [c for c in df.columns if c.startswith("BRENT_")]
colcap_cols = [c for c in df.columns if c.startswith("COLCAP_")]
trm_cols = [c for c in df.columns if c.startswith("TRM_")]
lab_cols = [c for c in df.columns if c.startswith("LAB_")]
emp_cols = [c for c in df.columns if c.startswith("EMP_")]

# --- 1. Series económicas continuas: interpolación + extrapolación ---
for col in pib_cols + ise_cols + ipc_cols + brent_cols:
    df[col] = df[col].interpolate(method='time')

    # Extrapolación lineal hacia atrás si faltan valores previos
    first_valid = df[col].first_valid_index()
    if first_valid:
        idx_first = df.index.get_loc(first_valid)
        if idx_first >= 1:
            # Calcular pendiente usando los dos primeros valores conocidos
            y1 = df[col].iloc[idx_first]
            y2 = df[col].iloc[idx_first + 1] if idx_first + 1 < len(df[col]) else y1
            x1 = idx_first
            x2 = idx_first + 1
            slope = y2 - y1  # cambio mensual aproximado
            for i in range(idx_first):
                df.iloc[i, df.columns.get_loc(col)] = y1 - slope * (x1 - i)

# --- 2. TRM y COLCAP: forward-fill y backward-fill ---
for col in trm_cols + colcap_cols:
    df[col] = df[col].ffill().bfill()

# --- 3. LAB y EMP: rellenar con 0 ---
for col in lab_cols + emp_cols:
    df[col] = df[col].fillna(0)

# Guardar la base completa
df.to_csv("base_central_completa_extrapolada.csv", encoding="utf-8")

print("✅ Base central completada con extrapolación para PIB e ISE.")
print("Rango de fechas:", df.index.min(), "a", df.index.max())

