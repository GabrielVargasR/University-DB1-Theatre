DELIMITER //

DROP PROCEDURE IF EXISTS sp_create_agente_user//
CREATE PROCEDURE sp_create_agente_user(
	IN pusername VARCHAR(30), 
    IN ppassw VARCHAR(40)
)
BEGIN

	DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Username repetido, intente con otro';
    END;
    
	SET @sqlcmd = CONCAT('CREATE USER ''', pusername, '''@''', 'localhost', '''IDENTIFIED BY ''', ppassw, ''';');
		PREPARE createUser FROM @sqlcmd;
		EXECUTE createUser;
		DEALLOCATE PREPARE createUser;
        
	SET @grantcmd = CONCAT('GRANT agente_teatro@localhost TO ''', pusername, '''@''', 'localhost', ''';');
        PREPARE grantRole FROM @grantcmd;
        EXECUTE grantRole;
        DEALLOCATE PREPARE grantRole;
        
	SET @defrole = CONCAT('SET DEFAULT ROLE ALL TO ''', pusername, '''@''', 'localhost', ''';');
        PREPARE setRole FROM @defrole;
        EXECUTE setRole;
        DEALLOCATE PREPARE setRole;
END//
DELIMITER ;