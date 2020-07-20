DELIMITER //

DROP PROCEDURE IF EXISTS sp_trn_comprar_tiquete//
CREATE PROCEDURE sp_trn_comprar_tiquete(
	IN pnum1 DECIMAL(3),
    IN pnum2 DECIMAL(3),
    IN pnum3 DECIMAL(3),
    IN pnum4 DECIMAL(3),
    IN pnum5 DECIMAL(3),
    IN pnum6 DECIMAL(3),
    IN pnum7 DECIMAL(3),
    IN pnum8 DECIMAL(3),
    IN ptitulo VARCHAR(40),
    IN pnom_bloque VARCHAR(20),
    IN pfila VARCHAR(1),
    IN pfecha DATETIME,
    IN pnombre VARCHAR(80),
    IN pmonto DECIMAL(10,2),
    IN pnum_validacion DECIMAL(6)
)

BEGIN
	DECLARE id_presentacion INT;
    DECLARE id_teatro INT;
    DECLARE id_asiento INT;
    DECLARE problema INT DEFAULT 0;
    DECLARE counter INT DEFAULT 1;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET problema = 1;
    
    SELECT c.id_presentacion, c.id_teatro
        INTO id_presentacion, id_teatro
        FROM v_cartelera AS c
        WHERE c.titulo = ptitulo AND c.fecha = pfecha;
    
    CREATE TABLE temp_asientos (
		num DECIMAL(3),
		id_asiento INT,
        counter INT
	);
    
    CREATE TRIGGER populate_temp AFTER INSERT ON temp_asientos FOR EACH ROW
		BEGIN
			DECLARE vid INT;
            IF NEW.num IS NOT NULL THEN
				SELECT a.id
				INTO vid
				FROM Asiento AS a
				WHERE a.numero = NEW.num AND a.fila = pfila AND a.teatro = id_teatro AND a.bloque = pbloque;
				
				UPDATE temp_asientos
					SET id = vid WHERE num = NEW.num;
			END IF;
        END;
	
    INSERT INTO temp_asientos(num, counter) VALUES (pnum1,1),(pnum2,2),(pnum3,3),(pnum4,4),(pnum5,5),(pnum6,6),(pnum7,7), (pnum8,8);
	
	START TRANSACTION;
		
        WHILE counter < 9 DO
			SELECT t.id_asiento
            INTO id_asiento
            FROM temp_asientos AS t
            WHERE t.counter = counter;
            
            IF id_asiento IS NOT NULL THEN
				UPDATE Disponibilidad AS d
				SET disponible = 0
				WHERE d.id_asiento = id_asiento AND
					  d.id_presentacion = id_presentacion;
			END IF;
            
			SET counter = counter +1;
        END WHILE;
        
        INSERT INTO Registro_Ventas(id_presentacion, nombre_cliente, monto, num_validacion, fecha) VALUES
								   (id_presentacion, pnombre, pmonto, pnum_validacion, pfecha);
                                   
		DROP TRIGGER IF EXISTS populate_temp;
		DROP TABLE IF EXISTS temp_asientos;
    
	IF problema THEN
		ROLLBACK;
	ELSE
		COMMIT;
	END IF;
    
    
END//
DELIMITER ;
