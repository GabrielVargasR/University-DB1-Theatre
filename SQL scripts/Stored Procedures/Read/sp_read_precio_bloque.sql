DELIMITER //

DROP PROCEDURE IF EXISTS sp_read_precio_bloque//
CREATE PROCEDURE sp_read_precio_bloque(
	IN titulo VARCHAR(40),
    IN fecha DATETIME,
    IN bloque VARCHAR(20),
    OUT precio DECIMAL(8,2)
)

BEGIN
	DECLARE id_teatro INT;
    DECLARE id_produccion INT;
    
    SELECT c.id_teatro, c.id_prod
    INTO id_teatro, id_produccion
    FROM v_cartelera AS c
    WHERE c.titulo = titulo AND c.fecha = fecha;
    
    IF id_produccion IS NOT NULL AND id_teatro IS NOT NULL THEN
		SELECT p.precio
		INTO precio
		FROM Precio AS p
		WHERE p.id_produccion = id_produccion AND 
			  p.nombre_bloque = bloque AND
			  p.id_teatro = id_teatro;
	END IF;
    
END //
DELIMITER ;