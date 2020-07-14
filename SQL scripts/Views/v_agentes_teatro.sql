DROP VIEW IF EXISTS v_agentes_teatro;
CREATE VIEW v_agentes_teatro AS
	SELECT a.cedula, a.nombre, a.fecha_nacimiento, a.sexo, a.direccion, a.tel_casa, a.celular, a.otro_tel, a.email, a.id_teatro, a.username
    FROM Agente_Teatro AS a
    WITH CHECK OPTION;