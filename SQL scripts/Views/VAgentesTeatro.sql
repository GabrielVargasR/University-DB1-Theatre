CREATE VIEW VAgentesTeatro AS
	SELECT a.cedula, a.nombre, a.fecha_nacimiento, a.sexo, a.direccion, a.tel_casa, a.celular, a.otro_tel, a.email, a.id_teatro, a.username
    FROM Agente_Teatro AS a;