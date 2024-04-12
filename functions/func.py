import csv
from db.connection import conectar as db


[conn, cursor] = db()

# Función para realizar acciones en la base de datos
def sql_table(sql, msj):
    try:
        # Se Ejecuta la sentencia SQL proporcionada
        cursor.execute(sql)
        # Se imprime un mensaje indicando que la acción se realizó correctamente
        print(msj)
    except Exception as e:
        # Se imprime un mensaje de error si ocurre alguna excepción durante la ejecución de la sentencia
        print("Error al ejecutar la sentencia", e)


# Función para abrir el archivo CSV y leer los datos
def read_csv(nombre_archivo):
    # Se inicializa una lista vacía para almacenar los datos del archivo CSV
    data = []
    # Se abre el archivo CSV en modo lectura
    with open(nombre_archivo, mode="r", newline='') as archivo_csv:
        # Se crea un lector de CSV para el archivo
        lector_csv = csv.reader(archivo_csv)
        # Se itera sobre cada fila en el archivo CSV
        for fila in lector_csv:
            data.append(fila)
    return data


# Función para abrir el archivo CSV y escribir los datos
def write_csv(nombre_archivo, localidades):
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo_csv:
                # Se crea un escritor de CSV
                writer = csv.writer(archivo_csv)  
                # Se itera sobre cada localidad y se la escribe en una fila del archivo CSV
                for localidad in localidades:
                    writer.writerow([localidad])
                # Se escribe la cantidad total de localidades al final del archivo
                archivo_csv.write(f'Total de localidades: {len(localidades)}')


# Defino la función para insertar los datos en la base de datos
def insert_data(nombre_archivo, sql):
    try:
        # Se leen los datos del archivo CSV
        datos_csv = read_csv(nombre_archivo)  
        #   Se itera por todas las filas menos la primera        
        for fila in datos_csv[1:]:
            try:
                # Ejecutar la sentencia SQL para insertar datos en la base de datos
                cursor.execute(sql, (fila[0], fila[1], fila[2], fila[3], fila[4]))
            except Exception as e:
                print("Error al insertar datos:", e)
        print("Se insertaron todos los datos")
        # Se confirman los cambios en la base de datos
        conn.commit()  
    except Exception as e:
        print("Error al insertar datos:", e)
