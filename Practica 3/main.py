import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="192.168.3.125",
        user="arturo",
        password="Pword1",
        database="distancia"
    )
    print("Conexión establecida exitosamente.")
    conexion.close()

except mysql.connector.Error as err:
    print("Error en la conexión:", err)
