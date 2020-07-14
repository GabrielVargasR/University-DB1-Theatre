DELIMITER //

DROP PROCEDURE IF EXISTS sp_read_asientos_disponibles//
CREATE PROCEDURE sp_read_asientos_disponibles(
	IN ptitulo_produccion VARCHAR(40),
    IN pfecha_presentacion DATETIME,
    IN pnombre_bloque VARCHAR(20)
)

BEGIN
	SELECT a.fila, a.numero
    FROM Disponibilidad AS d
		INNER JOIN Asiento AS a ON d.id_asiento = a.id
        INNER JOIN Bloque AS b ON a.bloque = b.nombre,
        Presentacion AS p INNER JOIN Produccion as pro ON p.id_produccion = pro.id
    WHERE d.disponible = 1 AND 
		  b.nombre = pnombre_bloque AND 
          pro.titulo = ptitulo_produccion AND
          p.fecha = pfecha_presentacion AND
          p.id = d.id_presentacion AND
          pro.estado = 4
    GROUP BY a.fila, a.numero
    ORDER BY a.numero;
END //

DELIMITER ;