# Se importa el módulo mariadb para la conexión a la base de datos
import mariadb

# Función para establecer la conexión con la base de datos
def conectar():
    try:
        # Se establece la conexión con la base de datos
        conn = mariadb.connect(
            user="your_user",
            password="your_password",
            host="localhost",
            port=3306, 
            database="name_database"
        )
        # Se crea un cursor para ejecutar consultas SQL
        cursor = conn.cursor()
        # Se devulve la conexión y el cursor como una lista
        return [conn, cursor]
    except Exception as e:
        print("Error de conexión a la base de datos", e)