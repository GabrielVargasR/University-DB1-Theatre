DELIMITER //

DROP PROCEDURE IF EXISTS sp_read_teatro_usuario//
CREATE PROCEDURE sp_read_teatro_usuario(
	IN pusuario VARCHAR(30),
    OUT pteatro INT
)

BEGIN
	SELECT u.id_teatro
	INTO pteatro
    FROM Usuario AS u
    WHERE u.username = pusuario;
END //

DELIMITER ;