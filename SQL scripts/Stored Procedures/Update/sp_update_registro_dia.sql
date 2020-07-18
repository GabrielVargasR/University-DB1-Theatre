DELIMITER //
DROP PROCEDURE IF EXISTS sp_update_registro_dia//
CREATE PROCEDURE sp_update_registro_dia()
BEGIN
	DECLARE precio DECIMAL(8,2);
    DECLARE cantidad INT;
    
    SELECT AVG(r.precio), COUNT(*)
    INTO precio, cantidad
    FROM Registro_Ventas AS r
    WHERE r.fecha = CURRENDT_DATE() - INTERVAL 1 DAY;
    
    INSERT INTO Registro_Dia(fecha, cantidad, costo_promedio) VALUES (CURRENDT_DATE() - INTERVAL 1 DAY, cantidad, precio);
END //
DELIMITER ;