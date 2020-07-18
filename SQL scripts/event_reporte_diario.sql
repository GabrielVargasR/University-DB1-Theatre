SET GLOBAL event_scheduler = ON;

CREATE EVENT reporte_diario
ON SCHEDULE EVERY 1 DAY
STARTS '2020-07-15 00:00:00'
DO
	CALL sp_update_registro_dia();