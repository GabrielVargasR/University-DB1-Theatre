DELIMITER //

DROP PROCEDURE IF EXISTS sp_trn_registrar_agente//
CREATE PROCEDURE sp_trn_registrar_agente(
	IN pid_teatro INT,
	IN pcedula DECIMAL(9),
    IN pnombre VARCHAR(80),
    IN pfecha_nacimiento DATE,
    IN psexo VARCHAR(1),
    IN pdireccion VARCHAR(100),
    IN ptel_casa DECIMAL(8),
    IN pcelular DECIMAL(8),
    IN potro_tel DECIMAL(8),
    IN pemail VARCHAR(50),
    IN pusername VARCHAR(30), 
    IN ppassw VARCHAR(40)
)

BEGIN
	DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Hubo un problema registrando el usuario';
		ROLLBACK;
    END;
        
	START TRANSACTION;
            
		INSERT INTO Usuario(cedula, nombre, fecha_nacimiento, sexo, direccion, tel_casa, celular, otro_tel, email, username, passw, id_teatro, tipo_usuario)
			VALUES(pcedula, pnombre, pfecha_nacimiento, psexo, pdireccion, ptel_casa, pcelular, potro_tel, pemail, pusername, ppassw, pid_teatro, 1);
    
		CALL sp_create_agente_user(pusername, ppassw);
		
    COMMIT;
END //
DELIMITER ;