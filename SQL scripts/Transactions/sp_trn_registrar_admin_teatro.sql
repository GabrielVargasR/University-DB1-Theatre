DELIMITER //

DROP PROCEDURE IF EXISTS sp_trn_registrar_admin_teatro//
CREATE PROCEDURE sp_trn_registrar_admin_teatro(
	IN pcedula DECIMAL(9),
    IN pnombre VARCHAR(80),
    IN pteatro VARCHAR(80),
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
	DECLARE teatro INT;
    
	DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Hubo un problema registrando el usuario';
		ROLLBACK;
    END;
        
	START TRANSACTION;
    
		SELECT t.id
			INTO teatro
			FROM Teatro as t
			WHERE t.nombre = pteatro;
            
		INSERT INTO Usuario(cedula, nombre, id_teatro, fecha_nacimiento, sexo, direccion, tel_casa, celular, otro_tel, email, username, passw, tipo_usuario)
        VALUES(pcedula, pnombre, teatro, pfecha_nacimiento, psexo, pdireccion, ptel_casa, pcelular, potro_tel, pemail, pusername, ppassw, 2);
    
		CALL sp_create_admin_user(pusername, ppassw);
		
    COMMIT;
END //
DELIMITER ;