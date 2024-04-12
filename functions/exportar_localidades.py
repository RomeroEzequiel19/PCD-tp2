import os, csv
from db.connection import conectar as db
from functions.func import write_csv

[conn, cursor] = db()

# Se crea un directorio para almacenar los archivos CSV de las provincias y localidades si no existe
output_dir = "provincias_csv"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# Función para agrupar las localidades por provincia y exportarlas a archivos CSV
def agrupar_localidades_provincia(sql):
    try:
        # Se crea diccionario para almacenar provincias y localidades
        localidades_provincia = {}  
        # Se ejecuta el sql para obtener las provincias y sus localidades
        cursor.execute(sql) 
        # Para obtener todos los datos de la consulta 
        datos = cursor.fetchall()  
        # Se itera sobre los datos y se agrupan las localidades por provincia
        for provincia, localidad in datos:
            if provincia in localidades_provincia:
                localidades_provincia[provincia].append(localidad)
            else:
                localidades_provincia[provincia] = [localidad]
        # Se llama a la función para exportar las localidades a archivos CSV
        exportar_a_csv(localidades_provincia)
    except Exception as e:
        print("Error al agrupar las localidades por provincia y exportar a archivos CSV:", e)


# Función para exportar las localidades por provincia a archivos CSV
def exportar_a_csv(localidades_provincia):
    try:
        # Se itera sobre cada provincia y sus localidades
        for provincia, localidades in localidades_provincia.items():
            # Si los nombres de las provincias poseen espacio, se las reemplaza por guión bajo
            nombre_archivo = os.path.join(output_dir, provincia.replace(" ", "_") + ".csv") 
            # Abrir el archivo CSV en modo escritura
            write_csv(nombre_archivo, localidades)
        print("Archivos CSV exportados exitosamente.")
    except Exception as e:
        print("Error al exportar los archivos CSV:", e)

