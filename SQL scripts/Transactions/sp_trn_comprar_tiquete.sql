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
    IN pnum_validacion DECIMAL(6), 
    IN pfecha_compra DATETIME
)

BEGIN
	DECLARE id_presentacion INT;
    DECLARE id_teatro INT;
    
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN 
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Asiento no está disponible';
        ROLLBACK;
    END;
	
	START TRANSACTION;
    
		SELECT c.id_presentacion, c.id_teatro
			INTO id_presentacion, id_teatro
			FROM v_cartelera AS c
			WHERE c.titulo = ptitulo AND c.fecha = pfecha;
		
        CALL sp_update_disponibilidad(id_teatro, id_presentacion, pnom_bloque, pfila, pnum1);
        CALL sp_update_disponibilidad(id_teatro, id_presentacion, pnom_bloque, pfila, pnum2);
        CALL sp_update_disponibilidad(id_teatro, id_presentacion, pnom_bloque, pfila, pnum3);
        CALL sp_update_disponibilidad(id_teatro, id_presentacion, pnom_bloque, pfila, pnum4);
        CALL sp_update_disponibilidad(id_teatro, id_presentacion, pnom_bloque, pfila, pnum5);
        CALL sp_update_disponibilidad(id_teatro, id_presentacion, pnom_bloque, pfila, pnum6);
        CALL sp_update_disponibilidad(id_teatro, id_presentacion, pnom_bloque, pfila, pnum7);
        CALL sp_update_disponibilidad(id_teatro, id_presentacion, pnom_bloque, pfila, pnum8);
        
        INSERT INTO Registro_Ventas(id_presentacion, nombre_cliente, monto, num_validacion, fecha) VALUES
								   (id_presentacion, pnombre, pmonto, pnum_validacion, pfecha_compra);

	COMMIT;
END//
DELIMITER ;
