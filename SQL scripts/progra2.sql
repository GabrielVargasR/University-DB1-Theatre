DROP DATABASE IF EXISTS progra2;
CREATE DATABASE progra2;

USE progra2;

CREATE TABLE Teatro(
	id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(80) NOT NULL,
    telefono DECIMAL(8) NOT NULL,
    website VARCHAR(100),
    tel_boleteria DECIMAL(8) NOT NULL,
    email VARCHAR(50),
    capacidad DECIMAL(8) NOT NULL,
    
    CONSTRAINT pk_teatro PRIMARY KEY(id),
    CONSTRAINT ak_teatro UNIQUE(nombre)
);

CREATE TABLE Agente_Teatro(
	cedula DECIMAL(9) NOT NULL,
    nombre VARCHAR(80) NOT NULL,
    fecha_nacimiento DATE,
    sexo VARCHAR(1),
    direccion VARCHAR(100),
    tel_casa DECIMAL(8),
    celular DECIMAL(8) NOT NULL,
    otro_tel DECIMAL(8),
    email VARCHAR(50),
    username VARCHAR(30) NOT NULL, 
    passw VARCHAR(40) NOT NULL,
    id_teatro INT NOT NULL,
    
    CONSTRAINT pk_agente_teatro PRIMARY KEY(cedula),
	CONSTRAINT fk_agente_teatro FOREIGN KEY(id_teatro) REFERENCES Teatro(id)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Administrador_Teatro(
	cedula DECIMAL(9) NOT NULL,
    nombre VARCHAR(80) NOT NULL,
    fecha_nacimiento DATE,
    sexo VARCHAR(1),
    direccion VARCHAR(100),
    tel_casa DECIMAL(8),
    celular DECIMAL(8) NOT NULL,
    otro_tel DECIMAL(8),
    email VARCHAR(50),
    username VARCHAR(30) NOT NULL, 
    passw VARCHAR(40) NOT NULL, 
    id_teatro INT NOT NULL,
    
    CONSTRAINT pk_admin_teatro PRIMARY KEY(cedula),
    CONSTRAINT fk_admin_teatro FOREIGN KEY(id_teatro) REFERENCES Teatro(id)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);


CREATE TABLE Administrador_Sistema(
	cedula DECIMAL(9) NOT NULL,
    nombre VARCHAR(80) NOT NULL,
    fecha_nacimiento DATE,
    sexo VARCHAR(1),
    direccion VARCHAR(100),
    tel_casa DECIMAL(8),
    celular DECIMAL(8) NOT NULL,
    otro_tel DECIMAL(8),
    email VARCHAR(50),
    username VARCHAR(30) NOT NULL, 
    passw VARCHAR(40) NOT NULL, 
    
    CONSTRAINT pk_admin_sistema PRIMARY KEY(cedula)
);

CREATE TABLE Tipo_Produccion(
	id INT NOT NULL AUTO_INCREMENT,
    tipo VARCHAR(30) NOT NULL,
    
    CONSTRAINT pk_tipo_prod PRIMARY KEY(id),
    CONSTRAINT ak_tipo_prod UNIQUE(tipo)
);

CREATE TABLE Estado_Produccion(
	id INT NOT NULL AUTO_INCREMENT,
    estado VARCHAR(30) NOT NULL,
    
    CONSTRAINT pk_estado_presentacion PRIMARY KEY(id),
    CONSTRAINT ak_estado_presentacion UNIQUE(estado)
);

CREATE TABLE Produccion(
	id INT NOT NULL AUTO_INCREMENT,
    id_teatro INT NOT NULL,
    titulo VARCHAR(40) NOT NULL,
    descripcion VARCHAR(200) NOT NULL,
    fecha_inicio DATE,
    fecha_fin DATE,
    tipo INT NOT NULL,
    estado INT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_produccion PRIMARY KEY(id),
    CONSTRAINT one_theatre_only UNIQUE(id_teatro, titulo, fecha_inicio),
    CONSTRAINT fk_produccion FOREIGN KEY(id_teatro) REFERENCES Teatro(id)
		ON DELETE RESTRICT
        ON UPDATE CASCADE,
	CONSTRAINT fk_produccion_tipo FOREIGN KEY(tipo) REFERENCES Tipo_Produccion(id)
		ON DELETE RESTRICT
        ON UPDATE CASCADE,
	CONSTRAINT fk_produccion_estado FOREIGN KEY(estado) REFERENCES Estado_Produccion(id)
		ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE Presentacion(
	id INT NOT NULL AUTO_INCREMENT,
    fecha DATETIME NOT NULL,
    id_teatro INT NOT NULL, 
    id_produccion INT NOT NULL,
    
    CONSTRAINT pk_presentacion PRIMARY KEY(id),
    CONSTRAINT ak_presentacion UNIQUE(fecha, id_produccion),
    CONSTRAINT fk_presentacion_teatro FOREIGN KEY(id_teatro) REFERENCES Teatro(id)
		ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT fk_presentacion_produccion FOREIGN KEY(id_produccion) REFERENCES Produccion(id)
		ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE Bloque(
	nombre VARCHAR(20) NOT NULL,
    id_teatro INT NOT NULL,
    
    CONSTRAINT pk_bloque PRIMARY KEY(nombre, id_teatro),
    CONSTRAINT fk_bloque_teatro FOREIGN KEY(id_teatro) REFERENCES Teatro(id)
		ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE Precio(
	id_produccion INT NOT NULL,
    nombre_bloque VARCHAR(20) NOT NULL,
    id_teatro INT NOT NULL,
    precio DECIMAL(8,2) NOT NULL,
    
    CONSTRAINT pk_precio PRIMARY KEY(id_produccion, nombre_bloque, id_teatro),
    CONSTRAINT fk_precio_produccion FOREIGN KEY (id_produccion) REFERENCES Produccion(id)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
	CONSTRAINT fk_precio_bloque FOREIGN KEY (nombre_bloque, id_teatro) REFERENCES Bloque(nombre, id_teatro)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Fila(
	letra VARCHAR(1) NOT NULL,
    cantidad_asientos DECIMAL(3),
    id_teatro INT NOT NULL,
    nombre_bloque VARCHAR(20) NOT NULL,
    
    CONSTRAINT pk_fila PRIMARY KEY(letra, id_teatro, nombre_bloque),
    CONSTRAINT fk_fila_bloque FOREIGN KEY(nombre_bloque, id_teatro) REFERENCES Bloque(nombre, id_teatro)
		ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE Asiento(
	id INT NOT NULL AUTO_INCREMENT,
	numero DECIMAL(3) NOT NULL,
    fila VARCHAR(1) NOT NULL,
    teatro INT NOT NULL,
    bloque VARCHAR(20) NOT NULL,
    
    CONSTRAINT pk_asiento PRIMARY KEY(id),
    CONSTRAINT ak_asiento UNIQUE(numero, fila, bloque, teatro),
    CONSTRAINT fk_asiento_fila FOREIGN KEY(fila, teatro, bloque) REFERENCES Fila(letra, id_teatro, nombre_bloque)
		ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE Disponibilidad(
	id_asiento INT NOT NULL,
    id_presentacion INT NOT NULL,
    disponible DECIMAL(1) NOT NULL DEFAULT 1, -- boolean value for True
    
    CONSTRAINT pk_disponibilidad PRIMARY KEY(id_asiento, id_presentacion),
    CONSTRAINT fk_disponibilidad_asiento FOREIGN KEY(id_asiento) REFERENCES Asiento(id)
		ON DELETE RESTRICT
        ON UPDATE CASCADE,
	CONSTRAINT fk_presentacion_asiento FOREIGN KEY(id_presentacion) REFERENCES Presentacion(id)
		ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE Registro_Ventas(
	consecutivo INT NOT NULL AUTO_INCREMENT,
	id_presentacion INT NOT NULL,
    precio DECIMAL (8,2) NOT NULL,
    fecha DATETIME NOT NULL DEFAULT NOW(),
    
    CONSTRAINT pk_registro PRIMARY KEY(consecutivo),
    CONSTRAINT fk_registro_presentcion FOREIGN KEY(id_presentacion) REFERENCES Presentacion(id)
		ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE Registro_Dia(
	fecha DATE NOT NULL,
    cantidad INT NOT NULL DEFAULT 0,
    costo_promedio DECIMAL(8,2),
    
    CONSTRAINT pk_reg_dia PRIMARY KEY(fecha)
);