CREATE TABLE IF NOT EXISTS empleados_rh (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(100) NOT NULL,
    correo_coorporativo varchar(100) NOT NULL UNIQUE,
    departamento varchar(100) NOT NULL,
    salario DECIMAL(10,2) NOT NULL,
    fecha_contratacion DATE NOT NULL
);