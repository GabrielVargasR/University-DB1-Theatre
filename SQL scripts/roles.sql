DROP ROLE IF EXISTS 'cliente'@'localhost', 'agente_teatro'@'localhost', 'admin_teatro'@'localhost', 'admin_sistema'@'localhost';
CREATE ROLE 'cliente'@'localhost', 'agente_teatro'@'localhost', 'admin_teatro'@'localhost', 'admin_sistema'@'localhost';

GRANT EXECUTE ON PROCEDURE progra2.sp_read_cartelera TO 'cliente'@'localhost', 'agente_teatro'@'localhost';
GRANT EXECUTE ON PROCEDURE progra2.sp_read_asientos_disponibles TO 'cliente'@'localhost', 'agente_teatro'@'localhost';
GRANT EXECUTE ON PROCEDURE progra2.sp_trn_comprar_tiquete TO 'cliente'@'localhost', 'agente_teatro'@'localhost';

GRANT EXECUTE ON PROCEDURE progra2.sp_create_nueva_produccion TO 'admin_teatro'@'localhost';
GRANT EXECUTE ON PROCEDURE progra2.sp_create_presentacion TO 'admin_teatro'@'localhost';
GRANT EXECUTE ON PROCEDURE progra2.sp_create_precio_bloque TO 'admin_teatro'@'localhost';
GRANT EXECUTE ON PROCEDURE progra2.sp_update_estado_produccion TO 'admin_teatro'@'localhost';
GRANT EXECUTE ON PROCEDURE progra2.sp_trn_registrar_agente TO 'admin_teatro'@'localhost';

GRANT ALL PRIVILEGES ON progra2.* TO 'admin_sistema'@'localhost';

CREATE USER 'cliente_teatro'@'localhost' IDENTIFIED BY 'cliente123';
GRANT 'cliente'@'localhost' TO 'cliente_teatro'@'localhost';
SET DEFAULT ROLE ALL TO 'cliente_teatro'@'localhost';

/*
DROP USER IF EXISTS 'juancho'@'localhost';
CREATE USER 'juancho'@'localhost' IDENTIFIED BY '12';
GRANT 'admin_teatro'@'localhost' TO 'juancho'@'localhost';
SET DEFAULT ROLE ALL TO 'juancho'@'localhost';
*/
