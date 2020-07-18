DELIMITER //
DROP PROCEDURE IF EXISTS sp_create_fila//
CREATE PROCEDURE sp_create_fila(
	IN pnombre_teatro INT,
    IN pnombre_bloque VARCHAR(20),
    IN pcantidad_asientos DECIMAL(3),
    IN pletra VARCHAR(1)
)

BEGIN
	DECLARE id_teatro INT;
    
    SELECT t.id
    INTO id_teatro
    FROM Teatro as t
    WHERE t.nombre = pnombre_teatro;
    
	INSERT INTO Fila(letra, cantidad_asientos, id_teatro, nombre_bloque) VALUES (pletra, pcantidad_asientos, id_teatro, pnombre_bloque);
    CALL sp_create_asientos(pcantidad_asientos, pletra, id_teatro, pnombre_bloque);
END//
DELIMITER ;