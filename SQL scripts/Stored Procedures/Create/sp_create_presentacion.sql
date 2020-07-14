DELIMITER //

DROP PROCEDURE IF EXISTS sp_create_presentacion//
CREATE PROCEDURE sp_create_presentacion(
	IN pid_teatro INT,
    IN ptitulo INT,
    IN pfecha DATETIME
)

BEGIN
	DECLARE id_produccion INT;
    
    SELECT p.id
    INTO id_produccion
    FROM Produccion AS p
    WHERE p.titulo = ptitulo AND p.id_teatro = pid_teatro AND p.estado IN (1,2,3,4);
    
    INSERT INTO Presentacion(fecha, id_teatro, id_produccion) VALUES (pfecha, pid_teatro, id_produccion);
    
    CALL sp_create_disponibles(LAST_INSERT_ID(), pid_teatro);
END //

DELIMITER ;