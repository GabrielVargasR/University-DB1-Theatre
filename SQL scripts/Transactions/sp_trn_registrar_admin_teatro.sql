DELIMITER //

DROP PROCEDURE IF EXISTS sp_trn_registrar_admin_teatro//
CREATE PROCEDURE sp_trn_registrar_admin_teatro(
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
			ROLLBACK;
		END;
        
	START TRANSACTION;
    
		SET @sqlcmd = CONCAT('CREATE USER ''', pusername, '''@''', 'localhost', '''IDENTIFIED BY ''', ppassw, ''';');
		PREPARE createUser FROM @sqlcmd;
		EXECUTE createUser;
		DEALLOCATE PREPARE createUser;
        
        SET @grantcmd = CONCAT('GRANT admin_teatro@localhost TO ''', pusername, '''@''', 'localhost', ''';');
        PREPARE grantRole FROM @grantcmd;
        EXECUTE grantRole;
        DEALLOCATE PREPARE grantRole;
        
        SET @defrole = CONCAT('SET DEFAULT ROLE ALL TO ''', pusername, '''@''', 'localhost', ''';');
        PREPARE setRole FROM @defrole;
        EXECUTE setRole;
        DEALLOCATE PREPARE setRole;
        
		INSERT INTO Administrador_Sistema(cedula, nombre, fecha_nacimiento, sexo, direccion, tel_casa, celular, otro_tel, email, username, passw)
        VALUES(pcedula, pnombre, pfecha_nacimiento, psexo, pdireccion, ptel_casa, pcelular, potro_tel, pemail, pussername, ppassw);
    COMMIT;
END //
DELIMITER ;