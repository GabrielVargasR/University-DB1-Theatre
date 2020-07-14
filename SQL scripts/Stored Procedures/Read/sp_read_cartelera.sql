DELIMITER //

DROP PROCEDURE IF EXISTS sp_read_cartelera//
CREATE PROCEDURE sp_read_cartelera(
	IN pfecha_inicio DATE,
    IN pfecha_fin DATE
)

BEGIN
    SELECT c.titulo, c.nombre, c.fecha, c.precios
    FROM v_cartelera AS c
    WHERE (DATE(c.fecha) BETWEEN pfecha_inicio AND pfecha_fin);
END //

DELIMITER ;