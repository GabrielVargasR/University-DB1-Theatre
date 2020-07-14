DELIMITER //
DROP PROCEDURE IF EXISTS sp_create_fila//
CREATE PROCEDURE sp_create_fila(
	IN pid_teatro INT,
    IN pnombre_bloque VARCHAR(20),
    IN pcantidad_asientos DECIMAL(3),
    IN pletra VARCHAR(1)
)

BEGIN
	INSERT INTO Fila(letra, cantidad_asientos, id_teatro, nombre_bloque) VALUES (pletra, pcantidad_asientos, pid_teatro, pnombre_bloque);
    CALL SPCreateAsientos(pcantidad_asientos, pletra, pid_teatro, pnombre_bloque);
END//
DELIMITER ;