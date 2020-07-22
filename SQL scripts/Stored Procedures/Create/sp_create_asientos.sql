DELIMITER //

DROP PROCEDURE IF EXISTS sp_create_asientos//
CREATE PROCEDURE sp_create_asientos(
	IN pcantidad_asientos DECIMAL(3),
    IN pletra_fila VARCHAR(1),
    IN pid_teatro INT,
    IN pnombre_bloque VARCHAR(20)
)

BEGIN
	DECLARE counter INT DEFAULT 0;
    
    WHILE counter < pcantidad_asientos DO
		SET counter = counter + 1;
		INSERT INTO Asiento(numero, fila, teatro, bloque) VALUES (counter, pletra_fila, pid_teatro, pnombre_bloque);
    END WHILE;
END//
DELIMITER ;