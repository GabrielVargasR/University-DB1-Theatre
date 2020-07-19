DELIMITER //

DROP FUNCTION IF EXISTS f_get_precios_produccion//
CREATE FUNCTION f_get_precios_produccion(
	pid_produccion INT,
    pid_teatro INT
) 
RETURNS VARCHAR(255) DETERMINISTIC
  
BEGIN
	DECLARE precios VARCHAR(255);
    DECLARE nombre VARCHAR(20);
    DECLARE precio DECIMAL (8,2);
    DECLARE hay_bloque INT DEFAULT 1;
    
    DECLARE cur_precios CURSOR FOR
		SELECT p.nombre_bloque, p.precio
        FROM Precio AS p
        WHERE p.id_produccion = pid_produccion AND p.id_teatro = pid_teatro;
        
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET hay_bloque = 0;
    
    OPEN cur_precios;
    
    FETCH cur_precios INTO nombre, precio;
    IF (hay_bloque) THEN
		SET precios = CONCAT(nombre, ': ', CONVERT(precio, CHAR));
		FETCH cur_precios INTO nombre, precio;
	ELSE
		SET precios = 'No se han definido precios para esta presentación';
	END IF;
    
    WHILE (hay_bloque) DO
		SET precios = CONCAT(precios, ', ', nombre, ': ', CONVERT(precio, CHAR));
        FETCH cur_precios INTO nombre, precio;
	END WHILE;
    
    CLOSE cur_precios;
    
    RETURN precios;
END //

DELIMITER ;