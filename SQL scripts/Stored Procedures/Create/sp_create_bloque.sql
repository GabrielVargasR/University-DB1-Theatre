DELIMITER //
DROP PROCEDURE IF EXISTS sp_create_bloque//
CREATE PROCEDURE sp_create_bloque(
	IN pnombre_bloque VARCHAR(20),
    IN pnombre_teatro VARCHAR(80)
)

BEGIN
	DECLARE id_teatro INT;
    
    SELECT t.id
    INTO id_teatro
    FROM Teatro as t
    WHERE t.nombre = pnombre_teatro;
    
    INSERT INTO Bloque(nombre, id_teatro) VALUES (pnombre_bloque, id_teatro);
END //
DELIMITER ;