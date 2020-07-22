DELIMITER //
DROP PROCEDURE IF EXISTS sp_update_registro_dia//
CREATE PROCEDURE sp_update_registro_dia()
BEGIN
	DECLARE precio DECIMAL(8,2) DEFAULT 0;
    DECLARE cantidad INT DEFAULT 0;
    
    SELECT AVG(r.monto), COUNT(*)
    INTO precio, cantidad
    FROM Registro_Ventas AS r
    WHERE DATE(r.fecha) = CURRENT_DATE() - INTERVAL 1 DAY;
    
    INSERT INTO Registro_Dia(fecha, cantidad, costo_promedio) VALUES (CURRENT_DATE() - INTERVAL 1 DAY, cantidad, precio);
END //
DELIMITER ;