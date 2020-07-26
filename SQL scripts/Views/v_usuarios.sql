DROP VIEW IF EXISTS v_usuarios;
CREATE VIEW v_usuarios AS
	SELECT a.cedula, a.nombre, a.fecha_nacimiento, a.sexo, a.direccion, a.tel_casa, a.celular, a.otro_tel, a.email, a.id_teatro, a.tipo_usuario, a.username
    FROM Usuario AS a
    WITH CHECK OPTION;