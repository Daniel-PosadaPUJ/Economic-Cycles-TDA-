import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# === 1. Cargar datos ===
df = pd.read_csv("base_macro_con_pib.csv")

# === 2. Identificar columnas numéricas (excepto fecha) ===
num_cols = [c for c in df.columns if c.lower() != "fecha"]

# === 3. Limpieza: quitar % y reemplazar comas por puntos ===
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

# === 5. Guardar las versiones escaladas ===
df_std.to_csv("macro_base_scaled.csv", index=False, encoding="utf-8")
df_minmax.to_csv("macro_base_normalize.csv", index=False, encoding="utf-8")

print("✅ Archivos 'macro_base_scaled.csv' y 'macro_base_normalize.csv' creados correctamente.\n")

# === 6. Graficar y guardar tres gráficos ===

# (1) Histogramas de las variables originales
plt.figure(figsize=(12, 8))
df[num_cols].hist(bins=20, figsize=(12, 8))
plt.tight_layout()
plt.savefig("grafico_distribuciones.png", dpi=300)
plt.close()
print("📊 Se guardó 'grafico_distribuciones.png'")

# (2) Matriz de correlación
plt.figure(figsize=(10, 8))
corr = df[num_cols].corr()
plt.imshow(corr, cmap="coolwarm", interpolation="none")
plt.colorbar(label="Correlación")
plt.xticks(range(len(num_cols)), num_cols, rotation=90)
plt.yticks(range(len(num_cols)), num_cols)
plt.title("Matriz de correlación")
plt.tight_layout()
plt.savefig("grafico_correlacion.png", dpi=300)
plt.close()
print("📈 Se guardó 'grafico_correlacion.png'")

# (3) Comparación de series (original, estandarizada y normalizada)
plt.figure(figsize=(12, 6))

# Gráfico de todas las variables originales
for col in num_cols:
    plt.plot(df[col], alpha=0.6, linewidth=1, label=col)

plt.title("Series Originales (valores en escala original)")
plt.xlabel("Observaciones")
plt.ylabel("Valor")
plt.legend(fontsize=8, ncol=3)
plt.tight_layout()
plt.savefig("grafico_series_originales.png", dpi=300)
plt.close()
print("📉 Se guardó 'grafico_series_originales.png'")

# Gráfico de todas las variables estandarizadas
plt.figure(figsize=(12, 6))
for col in num_cols:
    plt.plot(df_std[col], alpha=0.6, linewidth=1, label=col)

plt.title("Series Estandarizadas (media=0, varianza=1)")
plt.xlabel("Observaciones")
plt.ylabel("Valor estandarizado")
plt.legend(fontsize=8, ncol=3)
plt.tight_layout()
plt.savefig("grafico_series_estandarizadas.png", dpi=300)
plt.close()
print("📉 Se guardó 'grafico_series_estandarizadas.png'")

# Gráfico de todas las variables normalizadas
plt.figure(figsize=(12, 6))
for col in num_cols:
    plt.plot(df_minmax[col], alpha=0.6, linewidth=1, label=col)

plt.title("Series Normalizadas (valores entre 0 y 1)")
plt.xlabel("Observaciones")
plt.ylabel("Valor normalizado")
plt.legend(fontsize=8, ncol=3)
plt.tight_layout()
plt.savefig("grafico_series_normalizadas.png", dpi=300)
plt.close()
print("📉 Se guardó 'grafico_series_normalizadas.png'")

# (4) Serie temporal específica del PIB
if "PIB" in df.columns:
    plt.figure(figsize=(10, 5))
    plt.plot(df["PIB"], color="teal", linewidth=2)
    plt.title("Serie temporal del PIB")
    plt.xlabel("Observaciones")
    plt.ylabel("PIB")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("grafico_PIB.png", dpi=300)
    plt.close()
    print("📈 Se guardó 'grafico_PIB.png'")
else:
    print("⚠️ No se encontró la columna 'PIB' para graficar.")

print("\n✅ Todas las gráficas fueron guardadas como archivos PNG en el directorio actual.")

