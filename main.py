# Importo las distintas funciones a utilizar y la conexion a la base de datos
from db.connection import conectar as db
from functions.func import sql_table
from functions.func import insert_data
from functions.exportar_localidades import agrupar_localidades_provincia

# Conexión a la base de datos MariaDB
[conn, cursor] = db()


# Eliminar la tabla si existe
sql_drop_table = "DROP TABLE IF EXISTS provincias"
msj = "Se eliminó la base de datos"
#Se pasan como argumentos la sentencia sql y el mensaje
sql_table(sql_drop_table, msj)


# Crear la tabla en la base de datos
sql_create_table = "CREATE TABLE provincias (provincia VARCHAR(255),id INT,localidad VARCHAR(255),cp VARCHAR(255),id_prov_mstr VARCHAR(255))"
msj = "Se creó la base de datos"
#Se pasan como argumentos la sentencia sql y el mensaje
sql_table(sql_create_table, msj)


# Realizar las inserciones en la tabla
name_archive = "localidades.csv"
sql_insert_table = "INSERT INTO provincias (provincia, id, localidad, cp, id_prov_mstr) VALUES (?, ?, ?, ?, ?)"
# Se pasan como argumentos el nombre del archivo CSV y la sentencia sql
insert_data(name_archive, sql_insert_table)

# Exportar la información a un archivo CSV
sql_select_table = "SELECT provincia, localidad FROM provincias GROUP BY provincia, localidad"
# Se pasa como argumento la sentencia sql
agrupar_localidades_provincia(sql_select_table)

conn.close()


