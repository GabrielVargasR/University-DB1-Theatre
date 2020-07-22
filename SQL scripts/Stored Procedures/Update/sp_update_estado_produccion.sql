DELIMITER //

DROP PROCEDURE IF EXISTS sp_update_estado_produccion//
CREATE PROCEDURE sp_update_estado_produccion(
	IN pid_teatro INT,
    IN ptitulo VARCHAR(40),
    IN estado VARCHAR(30)
)

BEGIN
	DECLARE id_produccion INT;
    DECLARE id_estado INT DEFAULT 0;
    
    SELECT p.id
    INTO id_produccion
    FROM Produccion AS p
    WHERE p.titulo = ptitulo AND p.id_teatro = pid_teatro;
    
    SELECT e.id
    INTO id_estado
    FROM Estado_Produccion as e
    WHERE e.estado = estado;
    
    IF (id_estado != 0) THEN
        UPDATE Produccion SET estado = id_estado WHERE id = id_produccion;
	END IF;
END //
DELIMITER ;