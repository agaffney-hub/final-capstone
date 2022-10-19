
-- DROP TABLE IF EXISTS punt_game_df CASCADE;
-- DROP TABLE IF EXISTS punt_play_df CASCADE;
-- DROP TABLE IF EXISTS punt_pr_df CASCADE;
-- DROP TABLE IF EXISTS punt_pp_df CASCADE;
-- DROP TABLE IF EXISTS punt_ngs_df CASCADE;



-- Creating tables

CREATE TABLE punt_game_df (
	-- good
	gamekey INT,
	season_year INT,
	season_type VARCHAR(100),
	week INT,
	game_date VARCHAR(100),
	game_day VARCHAR(100),
	game_site VARCHAR(100),
	start_time VARCHAR(100),
	home_team VARCHAR(100),
	hometeamcode VARCHAR(100),
	visit_team VARCHAR(100),
	vistteamcode VARCHAR(100),
	stadium VARCHAR(100),
	stadiumtype VARCHAR(100),
	turf VARCHAR(100),
	gameweather VARCHAR(100),
	temperature FLOAT,
	outdoorweather VARCHAR(100),
	PRIMARY KEY (gamekey)
);

CREATE TABLE punt_play_df (
	--good
	season_year INT,
	season_type VARCHAR(100),
	gamekey INT,
	game_date VARCHAR(100),
	week INT,
	playid INT,
	game_clock VARCHAR(100),
	yardline VARCHAR(100),
	quarter INT,
	play_type VARCHAR(100),
	poss_team VARCHAR(100),
	home_team_visit_team VARCHAR(100),
	score_home_visiting VARCHAR(100),
	playdescription VARCHAR(1000),
		FOREIGN KEY (gamekey) REFERENCES punt_game_df (gamekey),
	PRIMARY KEY (gamekey, playid),
	UNIQUE (gamekey,playid)
);
CREATE TABLE punt_pr_df (
	--gooood
	season_year INT,
	gamekey INT,
	playid INT,
	gsisid INT,
	prole VARCHAR(100),
		FOREIGN KEY (gamekey) REFERENCES punt_game_df (gamekey),
	PRIMARY KEY(gamekey, playid, gsisid),
	UNIQUE(gamekey,playid,gsisid)
);


CREATE TABLE punt_ngs_df (
	season_year INT,
	gamekey INT,
	playid INT,
	gsisid INT,
	g_time VARCHAR(100),
	x FLOAT,
	y FLOAT,
	dis FLOAT,
	o FLOAT,
	dir FLOAT,
	g_event VARCHAR(100),
		FOREIGN KEY (gamekey) REFERENCES punt_game_df (gamekey),
		FOREIGN KEY (gsisid,playid,gamekey) REFERENCES punt_pr_df (gsisid,playid,gamekey),
	PRIMARY KEY (gsisid,playid,gamekey)
);


CREATE TABLE punt_pp_df (
	gsisid INT,
	p_number VARCHAR(100),
	p_position VARCHAR(100),
	PRIMARY KEY (gsisid,p_number),
	UNIQUE (gsisid,p_number)
);