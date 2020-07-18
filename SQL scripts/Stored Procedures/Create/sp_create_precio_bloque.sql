DELIMITER //

DROP PROCEDURE IF EXISTS sp_create_precio_bloque//
CREATE PROCEDURE sp_create_precio_bloque(
	IN pid_teatro INT,
    IN ptitulo VARCHAR(40),
    IN pnombre_bloque VARCHAR (20),
    IN pprecio DECIMAL(8,2)
)

BEGIN
	DECLARE id_produccion INT;
    
    SELECT p.id
    INTO id_produccion
    FROM Produccion AS p
    WHERE p.titulo = ptitulo AND p.id_teatro = pid_teatro AND p.estado IN (1,2,3);
    
    INSERT INTO Precio(id_produccion, nombre_bloque, id_teatro, precio) VALUES (id_produccion, pnombre_bloque, pid_teatro, pprecio);
    
END//
DELIMITER ;