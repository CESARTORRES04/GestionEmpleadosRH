from repositories import empleado_repository as repo

def listar_empleados_mejor_salario() -> list:
    empleados_salario = repo.listar_empleados()
    empleados_mejor_salario = []
    for empleado_salario in empleados_salario:
        if empleado_salario["salario"] > 20000:
            empleados_mejor_salario.append(empleado_salario)

    return  empleados_mejor_salario
    



if __name__ == "__main__":
    print("Listar empleados service \n")
    print(listar_empleados_mejor_salario())