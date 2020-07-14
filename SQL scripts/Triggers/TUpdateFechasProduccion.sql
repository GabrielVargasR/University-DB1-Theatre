DELIMITER //

DROP TRIGGER IF EXISTS TUpdateFechasProduccion//
CREATE TRIGGER TUpdateFechasProduccion AFTER INSERT ON Presentacion FOR EACH ROW
BEGIN
	DECLARE currentInicio DATE;
    DECLARE currentFin DATE;
    
    SELECT p.fecha_inicio, p.fecha_fin
    INTO currentInicio, currentFin
    FROM Produccion AS p
    WHERE p.id = NEW.id_produccion;
    
    IF (currentInicio IS NULL OR currentInicio > DATE(NEW.fecha)) THEN
		UPDATE Produccion
			SET fecha_inicio = DATE(NEW.fecha)
			WHERE Produccion.id = NEW.id_produccion;
	END IF;
    
    IF (currentFin IS NULL OR currentFin < DATE(NEW.fecha)) THEN
		UPDATE Produccion
			SET fecha_fin = DATE(NEW.fecha)
			WHERE Produccion.id = NEW.id_produccion;
	END IF;
    
END //
DELIMITER ;