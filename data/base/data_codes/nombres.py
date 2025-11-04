import pandas as pd

# === 1. Renombrar columnas de PIB ===
pib_map = {
    "Agricultura, ganadería, caza, silvicultura y pesca": "PIB_Agricultura",
    "Explotación de minas y canteras": "PIB_Mineria",
    "Industrias manufactureras": "PIB_Manufactura",
    "Suministro de electricidad, gas, vapor, aire acondicionado, tratamiento de aguas residuales, gestión de desechos y actividades de saneamiento ambiental": "PIB_Energia_Agua",
    "Construcción": "PIB_Construccion",
    "Comercio al por mayor y al por menor, reparación de vehículos automotores y motocicletas, transporte y almacenamiento, alojamiento y servicios de comida": "PIB_Comercio_Transp",
    "Información y comunicaciones": "PIB_InfoCom",
    "Actividades financieras y de seguros": "PIB_Financieras",
    "Actividades inmobiliarias": "PIB_Inmobiliarias",
    "Actividades profesionales, científicas y técnicas, actividades de servicios administrativos y de apoyo": "PIB_Profesionales",
    "Administración pública y defensa, planes de seguridad social de afiliación obligatoria, educación, actividades de atención de la salud humana y de servicios sociales": "PIB_Admin_Edu_Salud",
    "Actividades artísticas, de entretenimiento y recreación y otras actividades de servicios, actividades de los hogares individuales en calidad de empleadores, actividades no diferenciadas de los hogares individuales como productores de bienes y servicios para uso propio": "PIB_Arte_Otros",
    "Valor agregado bruto": "PIB_VAB",
    "Producto Interno Bruto": "PIB_PIB"
}

df_pib = pd.read_csv("pib_mensual.csv")
df_pib = df_pib.rename(columns=pib_map)
df_pib.to_csv("pib_mensual_renombrado.csv", index=False, encoding="utf-8")
print("✅ PIB columnas renombradas y guardadas en 'pib_mensual_renombrado.csv'")

# === 2. Renombrar columnas de ISE ===
ise_map = {
    "Actividades primarias": "ISE_Primarias",
    "Agricultura, ganadería, silvicultura y pesca": "ISE_Agricultura",
    "Minería y canteras": "ISE_Mineria",
    "Actividades secundarias": "ISE_Secundarias",
    "Industrias manufactureras": "ISE_Manufactura",
    "Construcción": "ISE_Construccion",
    "Actividades terciarias": "ISE_Terciarias",
    "Electricidad, gas, agua y saneamiento": "ISE_Energia_Agua",
    "Comercio, transporte, alojamiento y comida": "ISE_Comercio_Transp",
    "Información y comunicaciones": "ISE_InfoCom",
    "Servicios financieros y seguros": "ISE_Financieras",
    "Actividades inmobiliarias": "ISE_Inmobiliarias",
    "Servicios profesionales y administrativos": "ISE_Profesionales",
    "Administración pública, educación y salud": "ISE_Admin_Edu_Salud",
    "Arte, entretenimiento y otros servicios": "ISE_Arte_Otros",
    "Indicador de Seguimiento a la Economía (ISE)": "ISE_Indice"
}

df_ise = pd.read_csv("ise_tidy.csv")
df_ise = df_ise.rename(columns=ise_map)
df_ise.to_csv("ise_tidy_renombrado.csv", index=False, encoding="utf-8")
print("✅ ISE columnas renombradas y guardadas en 'ise_tidy_renombrado.csv'")
