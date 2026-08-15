from repositories.db import inicializar
from services import empleado_service as sve

def mostrar_emepleados_mejor_salario():
    inicializar()
    print(sve.listar_empleados_mejor_salario())


if __name__ == "__main__":
    print("Listar empleados main \n")
    mostrar_emepleados_mejor_salario()
