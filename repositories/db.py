import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        user = "kafka",
        password = "kafka123",
        database = "gestion_empleados_rh"
    )


def inicializar():
    conn = get_connection()
    cursor = conn.cursor()
    with open("gestionempleados.sql", "r", encoding="utf-8") as file:
        for sentencia in file.read().split(";"):
            if sentencia.strip():
                cursor.execute(sentencia)

    conn.commit()
    cursor.close()
    conn.close()
