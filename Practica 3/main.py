from conexion.conexion import Conexion

baseDeDatos = {
    "driver" : "MySql",
    "server" : "DESKTOP-GI8HMHT",  # Cambia esto a tu servidor SQL
    "database" : "IoT",  # Cambia esto a tu base de datos
    "usuario" : "",
    "contrasena" : "",
}

conection = Conexion(baseDeDatos)