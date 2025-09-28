import pandas as pd
import matplotlib.pyplot as plt

# === 1. Leer CSV mensual interpolado ===
df = pd.read_csv("pib_mensual.csv")

# Limpiar y convertir Fecha
df["Fecha"] = pd.to_datetime(
    df["Fecha"].astype(str).str.strip().str.replace(r"[^0-9\-]", "", regex=True),
    format="%Y-%m",
    errors="coerce"
)

# === 2. Leer CSV trimestral original ===
df_trimestral = pd.read_csv("pib_tidy.csv")

# Limpiar y convertir Fecha
df_trimestral["Fecha"] = pd.to_datetime(
    df_trimestral["Fecha"].astype(str).str.strip().str.replace(r"[^0-9\-]", "", regex=True),
    format="%Y-%m",
    errors="coerce"
)

# Verificar fechas inválidas
if df_trimestral["Fecha"].isna().any():
    print("⚠️ Fechas inválidas en CSV trimestral:", df_trimestral.loc[df_trimestral["Fecha"].isna(), "Fecha"])

# === 3. Seleccionar columna de interés ===
columna = "Producto Interno Bruto"

# === 4. Graficar ===
plt.figure(figsize=(12, 5))
plt.scatter(df_trimestral["Fecha"], df_trimestral[columna], color="red", label="Trimestral (original)")
plt.plot(df["Fecha"], df[columna], color="blue", label="Interpolación mensual")

plt.title("Interpolación mensual del Producto Interno Bruto")
plt.xlabel("Fecha")
plt.ylabel(columna)
plt.legend()
plt.grid(True)

# === 5. Guardar imagen ===
plt.tight_layout()
plt.savefig("interpolacion_PIB.png", dpi=300)
plt.close()  # cerrar figura para liberar memoria

print("✅ Imagen guardada como 'interpolacion_PIB.png'")

