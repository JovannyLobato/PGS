CREATE DATABASE IF NOT EXISTS registro_huellas;
USE registro_huellas;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    id_huella VARCHAR(255) UNIQUE NOT NULL,
    fecha_nacimiento DATE,
    rol ENUM('niño', 'administrador') DEFAULT 'niño'
);

CREATE TABLE IF NOT EXISTS registros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    tipo ENUM('entrada', 'salida') NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);


-- usuarios de ejemplos
INSERT INTO usuarios (nombre, apellido, id_huella, fecha_nacimiento, rol)
VALUES ('Lupita', 'Gómez', 'huella_001', '2015-06-12', 'niño');

INSERT INTO usuarios (nombre, apellido, id_huella, fecha_nacimiento, rol)
VALUES ('Carlos', 'Ramírez', 'huella_002', '2014-09-25', 'niño');

INSERT INTO usuarios (nombre, apellido, id_huella, fecha_nacimiento, rol)
VALUES ('Ana', 'Martínez', 'huella_003', '1990-02-10', 'administrador');

select * from usuarios;
select * registros;