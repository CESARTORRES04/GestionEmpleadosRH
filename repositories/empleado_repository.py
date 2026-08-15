from repositories.db import get_connection
from repositories.db import inicializar
from models.empleado import Empleado

def listar_empleados() -> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM empleados_rh")
    filas = cursor.fetchall()
    cursor.close()
    conn.close()

    return [Empleado.from_row(fila) for fila in filas]


if __name__ == "__main__":
    print("Listar empleados \n")
    print(listar_empleados())