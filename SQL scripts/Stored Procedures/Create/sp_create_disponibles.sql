DELIMITER //

DROP PROCEDURE IF EXISTS sp_create_disponibles//
CREATE PROCEDURE sp_create_disponibles(
	IN pid_presentacion INT,
    IN pid_teatro INT
)

BEGIN
	DECLARE asiento INT;
	DECLARE hayAsientos INT DEFAULT 1;

	DECLARE cur_asientos CURSOR FOR 
		SELECT a.id
        FROM Asiento AS a
        WHERE a.teatro = pid_teatro;
	
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET hayAsientos = 0;
    
    OPEN cur_asientos;
    

    FETCH cur_asientos INTO asiento;
    
    WHILE (hayAsientos) DO
        INSERT INTO Disponibilidad(id_asiento, id_presentacion, disponible) VALUES (asiento, pid_presentacion, 1);
        FETCH cur_asientos INTO asiento;
	END WHILE;
    
    CLOSE cur_asientos;
    
END//
DELIMITER ;