DROP VIEW IF EXISTS v_cartelera;
CREATE VIEW v_cartelera AS
	SELECT pro.id AS id_prod, pre.id AS id_presentacion, pro.titulo AS titulo, t.id AS id_teatro, t.nombre AS nombre, pre.fecha AS fecha, f_get_precios_produccion(pro.id, t.id) AS precios
		FROM Teatro AS t INNER JOIN (Produccion AS pro INNER JOIN Presentacion AS pre ON pre.id_produccion = pro.id) ON t.id = pro.id_teatro
		WHERE pro.estado IN (2,3,4)
        WITH CHECK OPTION;
