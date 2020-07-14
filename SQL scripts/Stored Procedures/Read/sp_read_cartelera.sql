DELIMITER //

DROP PROCEDURE IF EXISTS sp_read_cartelera//
CREATE PROCEDURE sp_read_cartelera(
	IN pfecha_inicio DATE,
    IN pfecha_fin DATE
)

BEGIN
	-- estados posibles 2, 3, 4 (adelantada, anunciada, abierta)
    DECLARE precios VARCHAR(255);
    
    SELECT pro.titulo, t.nombre, pre.fecha, f_get_precios_produccion(pro.id, t.id)
    FROM Teatro AS t INNER JOIN (Produccion AS pro INNER JOIN Presentacion AS pre ON pre.id_produccion = pro.id) ON t.id = pro.id_teatro
    WHERE (DATE(pre.fecha) BETWEEN pfecha_inicio AND pfecha_fin) AND pro.estado IN (2,3,4);
END //

DELIMITER ;