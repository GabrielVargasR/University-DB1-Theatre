DELIMITER //

DROP PROCEDURE IF EXISTS sp_create_teatro//
CREATE PROCEDURE sp_create_teatro(
	IN pnombre VARCHAR(80),
	IN ptelefono DECIMAL(8,0),
	IN pwebsite VARCHAR(100),
	IN ptel_boleteria DECIMAL(8,0),
	IN pemail VARCHAR(50),
	IN pcapacidad DECIMAL(8,0)
)

BEGIN
	INSERT INTO Teatro(nombre, telefono, website, tel_boleteria, email, capacidad) 
			VALUES (pnombre, ptelefono, pwebsite, ptel_boleteria, pemail, pcapacidad);
END //
DELIMITER ;