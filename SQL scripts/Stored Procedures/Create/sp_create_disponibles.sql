DELIMITER //

DROP PROCEDURE IF EXISTS sp_create_disponibles//
CREATE PROCEDURE sp_create_disponibles(
	IN pid_presentacion INT,
    IN pid_teatro INT
)

BEGIN
	DECLARE asiento INT;
	DECLARE hayAsientos INT DEFAULT TRUE;

	DECLARE cur_asientos CURSOR FOR 
		SELECT a.id
        FROM Asiento AS a
        WHERE a.teatro = pid_teatro;
	
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET hayAsientos = FALSE;
    
    OPEN cur_asientos;
    
    FETCH cur_asientos INTO asiento;
    IF (hayAsiento) THEN
		INSERT INTO Disponibilidad(id_asiento, id_presentacion, disponible) VALUES (asiento, pid_presenntacion, 1);
	END IF;
    
    WHILE (hayAsiento) DO
		FETCH cur_asientos INTO asiento;
        INSERT INTO Disponibilidad(id_asiento, id_presentacion, disponible) VALUES (asiento, pid_presenntacion, 1);
	END WHILE;
    
    CLOSE cur_asientos;
    
END//
DELIMITER ;