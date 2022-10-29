CREATE TABLE punt_analytics AS
SELECT
	ppr.gamekey, 
	ppr.playid, 
	ppr.gsisid,
	pi.season_type, 
	pi.quarter, 
	pi.score_home_visiting, 
	gms.stadiumtype, 
	gms.turf, 
	gms.gameweather, 
	gms.temperature, 
	pp.p_position
FROM play_player_role AS ppr
INNER JOIN play_info AS pi
	ON (ppr.gamekey = pi.gamekey AND  ppr.playid = pi.playid)
LEFT JOIN game_data AS gms
	ON (ppr.gamekey = gms.gamekey)
LEFT JOIN player_punt_data AS pp
	ON (ppr.gsisid = pp.gsisid)
;

