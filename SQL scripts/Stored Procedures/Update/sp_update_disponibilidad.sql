DELIMITER //

DROP PROCEDURE IF EXISTS sp_update_disponibilidad//
CREATE PROCEDURE sp_update_disponibilidad(
	IN pid_teatro INT,
    IN pid_presentacion INT,
    IN pnom_bloque VARCHAR(20),
    IN pfila VARCHAR(1),
    IN pnumero DECIMAL(3)
)

BEGIN
	DECLARE id_asiento INT;
    DECLARE disponible INT DEFAULT 0;
    
    IF pnumero IS NOT NULL THEN
		SELECT a.id
			INTO id_asiento
			FROM Asiento AS a
			WHERE a.teatro = pid_teatro AND
				  a.bloque = pnom_bloque AND
				  a.fila = pfila AND
				  a.numero = pnumero;
                  
		SELECT d.disponible 
        INTO disponible 
        FROM Disponibilidad AS d
        WHERE d.id_asiento = id_asiento AND
				  d.id_presentacion = pid_presentacion;
		
        IF disponible = 1 THEN
			UPDATE Disponibilidad AS d
				SET disponible = 0
				WHERE d.id_asiento = id_asiento AND
					  d.id_presentacion = pid_presentacion;
		ELSE
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Asiento no está disponible';
        END IF;
	END IF;
    
END //
DELIMITER ;