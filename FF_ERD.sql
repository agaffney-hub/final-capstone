-- DROP TABLE IF EXISTS FF_play_df CASCADE;
-- DROP TABLE IF EXISTS FF_inj_df CASCADE;
-- DROP TABLE IF EXISTS FF_plyr_df CASCADE;

-- Creating tables
CREATE TABLE FF_play_df (
	 FF_playerkey INT ,
     FF_gameid VARCHAR(50),
	 FF_playkey VARCHAR(50),
	 FF_rosterposition VARCHAR(50),
	 FF_playerday INT,
	 FF_playergame INT,
	 FF_stadiumtype VARCHAR(50),
	 FF_fieldtype  VARCHAR(50),
	 FF_temperature INT,
	 FF_weather VARCHAR(250),
	 FF_playtype VARCHAR(50),
	 FF_playergameplay INT,
	 FF_position VARCHAR(50),
	 FF_postiongroup VARCHAR(50),
	 PRIMARY KEY (FF_playkey)
);



CREATE TABLE FF_inj_df (
     FF_playerkey INT,
     FF_gameid VARCHAR(50),
	 FF_playkey VARCHAR(50) ,
	 FF_bodypart VARCHAR(50),
	 FF_fieldtype VARCHAR(50),
	DM_M1 INT,
	DM_M7 INT,
	DM_M28 INT,
	DM_M42 INT,
	PRIMARY KEY (FF_playkey),
	 FOREIGN KEY (FF_playkey) REFERENCES FF_play_df(FF_playkey)
);



CREATE TABLE FF_plyr_df (
	 FF_playkey VARCHAR(50),
	 FF_time FLOAT8 ,
	 FF_event VARCHAR(50) ,
	 FF_x FLOAT8 ,
	 FF_y FLOAT8 ,
	 FF_dir FLOAT8 ,
	 FF_dis FLOAT8 ,
	 FF_O FLOAT8 ,
	 FF_s FLOAT8 ,
	PRIMARY KEY (FF_playkey),
     FOREIGN KEY (FF_playkey) REFERENCES FF_play_df(FF_playkey)
);