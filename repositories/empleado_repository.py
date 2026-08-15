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


def actualizar_salario(correo_coorporativo, nuevo_salario):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE empleados_rh SET salario = %s where correo_coorporativo = %s", (nuevo_salario, correo_coorporativo))
    conn.commit()
    afectadas = cursor.rowcount
    cursor.close()
    conn.close()
    return afectadas > 0

if __name__ == "__main__":
    print("Actualizar Salario \n")
    print(actualizar_salario("pedro@meta.com",11000.0))