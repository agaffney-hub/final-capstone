
-- DROP TABLE IF EXISTS FF_play_df CASCADE;
-- DROP TABLE IF EXISTS FF_inj_df CASCADE;
-- DROP TABLE IF EXISTS FF_plyr_df CASCADE;

CREATE TABLE FF_play_df (
	playerkey INT ,
  	gameid VARCHAR(50),
	playkey VARCHAR(50),
	rosterposition VARCHAR(50),
	playerday INT,
	playergame INT,
	stadiumtype VARCHAR(50),
	fieldtype  VARCHAR(50),
	temperature INT,
	weather VARCHAR(250),
	playtype VARCHAR(50),
	playergameplay INT,
	p_position VARCHAR(50),
	postiongroup VARCHAR(50),
	PRIMARY KEY (playkey)
);



CREATE TABLE FF_inj_df (
    playerkey INT,
    gameid VARCHAR(50),
	playkey VARCHAR(50) ,
	bodypart VARCHAR(50),
	fieldtype VARCHAR(50),
	DM_M1 INT,
	DM_M7 INT,
	DM_M28 INT,
	DM_M42 INT,
	PRIMARY KEY (playkey),
	FOREIGN KEY (playkey) REFERENCES FF_play_df(playkey)				 
);



CREATE TABLE FF_plyr_df (
	playkey VARCHAR(50),
	time FLOAT ,
	event VARCHAR(50) ,
	x FLOAT ,
	y FLOAT ,
	dir FLOAT ,
	dis FLOAT ,
	O FLOAT ,
	s FLOAT ,
	PRIMARY KEY (playkey),
    FOREIGN KEY (playkey) REFERENCES FF_play_df(playkey),
	UNIQUE (playkey,time)
);
