import pandas as pd

# Cargar el archivo (debe estar en la misma carpeta que este script)
data = pd.read_excel("je_conteo_20250731.xlsx", sheet_name="CONTEO")

# Quitar duplicados
data = data.drop_duplicates()

# Rellenar valores nulos con "SIN DATO"
data = data.fillna("SIN DATO")

# Estandarizar localidades en mayúsculas
data["LOCALIDAD"] = data["LOCALIDAD"].str.upper()

# ---- Análisis básico ----
# 1. Número de estudiantes por localidad
print("Estudiantes por localidad:")
print(data["LOCALIDAD"].value_counts(), "\n")

# 2. Proporción hombres/mujeres
print("Proporción por sexo:")
print(data["SEXO"].value_counts(normalize=True) * 100, "\n")

# 3. Beneficiarios por sector del colegio
print("Beneficiarios por sector del colegio:")
print(data.groupby("SECTOR COLEGIO GRADUACION MEDIA")["BENEFICIARIOS DEL PROGRAMA"].sum())
