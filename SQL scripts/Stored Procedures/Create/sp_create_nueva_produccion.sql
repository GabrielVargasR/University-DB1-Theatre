DELIMITER //

DROP PROCEDURE IF EXISTS sp_create_nueva_produccion//

CREATE PROCEDURE sp_create_nueva_produccion(
	IN ptitulo 	VARCHAR(40),
    IN pdescripcion VARCHAR(200),
    IN ptipo VARCHAR(30),
    IN pid_teatro INT
)

BEGIN
	INSERT INTO Produccion(id_teatro, titulo, descripcion, tipo) VALUES(pid_teatro, ptitulo, pdescripcion, ptipo);
END //

DELIMITER ;