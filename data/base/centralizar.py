import pandas as pd

nombres = [         # COLUMNAS
    "trm_mensual.csv", # Periodo | TRM.
    "relab_sector_tidy.csv", # Fecha | Agricultura | Minas | Manufactura | Energia_Agua | Construccion | Comercio | Transporte | Alojamiento_Comida | Info_Comunicaciones | Financieras | Inmobiliarias | Profesionales | AdmPublica_Salud | Arte_Otros.
    "relab_publico_privado_tidy.csv", # Fecha | Hombre_Público | Mujeres_Público | Hombre_Privado | Mujeres_Privado
    "relab_dependientes_independientes_tidy.csv", # Fecha, Dependientes, Independientes
    "pib_mensual.csv", # Fecha | Agricultura, ganadería, caza, silvicultura y pesca	| Explotación de minas y canteras | Industrias manufactureras | Suministro de electricidad, gas, vapor, aire acondicionado, tratamiento de aguas residuales, gestión de desechos y actividades de saneamiento ambiental | Construcción | Comercio al por mayor y al por menor, reparación de vehículos automotores y motocicletas, transporte y almacenamiento, alojamiento y servicios de comida | Información y comunicaciones | Actividades financieras y de seguros	Actividades inmobiliarias	Actividades profesionales, científicas y técnicas, actividades de servicios administrativos y de apoyo	Administración pública y defensa, planes de seguridad social de afiliación obligatoria, educación, actividades de atención de la salud humana y de servicios sociales | Actividades artísticas, de entretenimiento y recreación y otras actividades de servicios, actividades de los hogares individuales en calidad de empleadores, actividades no diferenciadas de los hogares individuales como productores de bienes y servicios para uso propio | Valor agregado bruto | Producto Interno Bruto.
    "ise_tidy.csv", # Fecha | Actividades primarias | Agricultura, ganadería, silvicultura y pesca | Minería y canteras | Actividades secundarias | Industrias manufactureras | Construcción	Actividades terciarias | Electricidad, gas, agua y saneamiento | Comercio, transporte, alojamiento y comida	Información y comunicaciones | Servicios financieros y seguros |	Actividades inmobiliarias | Servicios profesionales y administrativos | Administración pública, educación y salud | Arte, entretenimiento y otros servicios | Indicador de Seguimiento a la Economía (ISE).
    "ipc_tidy.csv", # Periodo | IPC_mensual.
    "colcap_tidy.csv", # Fecha | Valor_COLCAP | Pct_var_COLCAP.
    "brent_tidy.csv", # Fecha | Precio_Brent_USD | Pct_var_brent.
    "aportantes_empresas.csv" #Periodo | microempresas | pequeñas_emp | medianas_emp | grandes_emp.
]

# Lista de archivos y prefijos solo para los que no tienen prefijo todavía
documentos = [
    ("trm_mensual.csv", "TRM"),
    ("relab_sector_tidy.csv", "LAB"),
    ("relab_publico_privado_tidy.csv", "LAB"),
    ("relab_dependientes_independientes_tidy.csv", "LAB"),
    ("pib_mensual_renombrado.csv", None),  # Ya tiene prefijos
    ("ise_tidy_renombrado.csv", None),     # Ya tiene prefijos
    ("ipc_tidy.csv", "IPC"),
    ("colcap_tidy.csv", "COLCAP"),
    ("brent_tidy.csv", "BRENT"),
    ("aportantes_empresas.csv", "EMP")
]

# DataFrame central vacío
df_central = pd.DataFrame()

for archivo, prefijo in documentos:
    # Leer CSV
    df = pd.read_csv(archivo)

    # Detectar columna de fecha
    fecha_col = [c for c in df.columns if "fecha" in c.lower() or "periodo" in c.lower()]
    if not fecha_col:
        raise ValueError(f"No se encontró columna de fecha en {archivo}")
    fecha_col = fecha_col[0]

    # Convertir a datetime
    df[fecha_col] = pd.to_datetime(
        df[fecha_col].astype(str).str.strip().str.replace(r"[^0-9\-]", "", regex=True),
        format="%Y-%m",
        errors="coerce"
    )

    df = df.set_index(fecha_col)

    # Agregar prefijo solo si está definido
    if prefijo is not None:
        df = df.add_prefix(f"{prefijo}_")

    # Concatenar al DataFrame central
    if df_central.empty:
        df_central = df
    else:
        df_central = pd.concat([df_central, df], axis=1)

# Ordenar por fecha
df_central = df_central.sort_index()

# Guardar la base central
df_central.to_csv("base_central.csv", encoding="utf-8")

print("✅ Base central creada con columnas:")
print(df_central.columns.tolist())
print("Rango de fechas:", df_central.index.min(), "a", df_central.index.max())

