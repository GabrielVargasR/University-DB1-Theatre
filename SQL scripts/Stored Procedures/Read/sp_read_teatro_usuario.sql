DELIMITER //

DROP PROCEDURE IF EXISTS sp_read_teatro_usuario//
CREATE PROCEDURE sp_read_teatro_usuario(
	IN usuario VARCHAR(30),
    IN tipo INT,
    OUT teatro INT
)

BEGIN
	IF tipo = 0 THEN
		SELECT a.id_teatro
        INTO teatro
        FROM Administrador_Teatro as a
        WHERE a.username = usuario;
    ELSEIF tipo = 1 THEN
		SELECT agt.id_teatro
        INTO teatro
        FROM Agente_Teatro as agt
        WHERE agt.username = usuario;
    END IF;
END //

DELIMITER ;