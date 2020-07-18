DELIMITER //

DROP PROCEDURE IF EXISTS sp_trn_comprar_tiquete//
CREATE PROCEDURE sp_trn_comprar_tiquete(
	IN pnum DECIMAL(3),
    IN pid_teatro INT,
    IN pnom_bloque VARCHAR(20),
    IN pfila VARCHAR(1),
    IN pfecha DATETIME,
    IN ptitulo VARCHAR(40)
)

BEGIN
	DECLARE id_presentacion INT;
    DECLARE id_asiento INT;
    DECLARE precio DECIMAL(8,2);
    
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
		BEGIN
			ROLLBACK;
		END;
        
	START TRANSACTION;
        
        SELECT pre.id
			INTO id_presentacion
			FROM Produccion AS pro INNER JOIN Presentacion AS pre ON pro.id = pre.produccion
			WHERE pre.fecha = pfecha;
    
		SELECT a.id
			INTO id_asiento
			FROM Asiento AS a
			WHERE a.teatro = pid_teatro AND
				  a.bloque = pnom_bloque AND
				  a.fila = pfila AND
				  a.numero = pnum;
                  
		SELECT p.precio
			INTO precio
            FROM Precio AS p INNER JOIN Produccion AS pro ON p.id_produccion = pro.id
            WHERE p.id_teatro = pid_teatro AND
				  p.nombre_bloque = pnom_bloque AND
                  pro.titulo = ptitulo;
    
		UPDATE Disponibilidad AS d
			SET disponible = 0
			WHERE d.id_asiento = id_asiento AND
			      d.id_presentacion = id_presentacion;
                  
		INSERT INTO Registro_Ventas(id_presentacion, precio) VALUES(id_presentacion, precio);
                  
	COMMIT;
END//
DELIMITER ;
