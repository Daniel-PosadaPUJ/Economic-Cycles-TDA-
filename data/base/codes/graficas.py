import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# === 1. Cargar datos ===
df = pd.read_csv("base_macro_con_pib.csv")

# === 2. Identificar y procesar columna de fecha ===
fecha_col = [c for c in df.columns if c.lower() in ["fecha", "date", "periodo"]]
if fecha_col:
    fecha_col = fecha_col[0]
    df[fecha_col] = pd.to_datetime(df[fecha_col], errors="coerce")
    df = df.sort_values(fecha_col)
    df = df.set_index(fecha_col)
else:
    print("⚠️ No se encontró columna de fecha, se usará índice numérico.")
    df.index = range(len(df))

# === 3. Limpieza de datos numéricos ===
num_cols = [c for c in df.columns if df[c].dtype != "O"]

for col in num_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace("%", "", regex=False)
        .str.replace(",", ".", regex=False)
    )
    df[col] = pd.to_numeric(df[col], errors="coerce")

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

# === 5. Función auxiliar para formatear eje X ===
def configurar_eje_fechas(ax):
    ax.xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=10))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    plt.xticks(rotation=45)
    plt.tight_layout()

# === 6. Gráfico de series estandarizadas ===
plt.figure(figsize=(12, 6))
for col in num_cols:
    plt.plot(df_std.index, df_std[col], linewidth=1.2, label=col)
plt.title("Series Estandarizadas (Z-score)")
plt.xlabel("Fecha" if fecha_col else "Observaciones")
plt.ylabel("Valor Estandarizado")
plt.legend(fontsize=7, ncol=3)
plt.grid(alpha=0.4)
if fecha_col:
    configurar_eje_fechas(plt.gca())
plt.tight_layout()
plt.savefig("grafico_series_estandarizadas.png", dpi=300)
plt.close()
print("📊 Se guardó 'grafico_series_estandarizadas.png'")

# === 7. Gráfico de series normalizadas ===
plt.figure(figsize=(12, 6))
for col in num_cols:
    plt.plot(df_minmax.index, df_minmax[col], linewidth=1.2, label=col)
plt.title("Series Normalizadas (Min-Max)")
plt.xlabel("Fecha" if fecha_col else "Observaciones")
plt.ylabel("Valor Normalizado [0, 1]")
plt.legend(fontsize=7, ncol=3)
plt.grid(alpha=0.4)
if fecha_col:
    configurar_eje_fechas(plt.gca())
plt.tight_layout()
plt.savefig("grafico_series_normalizadas.png", dpi=300)
plt.close()
print("📈 Se guardó 'grafico_series_normalizadas.png'")

print("\n✅ Gráficas generadas con fechas espaciadas y guardadas correctamente.")

