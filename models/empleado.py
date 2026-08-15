from dataclasses import dataclass
from datetime import date

@dataclass
class Empleado:
    id: int
    nombre: str
    correo_coorporativo: str
    departamento: str
    salario: float
    fecha_contratacion: date

    @classmethod
    def from_row(cls, row:dict) -> "Empleado":
        return cls(
            id=row["id"],
            nombre=row["nombre"],
            correo_coorporativo=row["correo_coorporativo"],
            departamento=row["departamento"],
            salario=float(row["salario"]),
            fecha_contratacion=row["fecha_contratacion"],
        )
