DROP TABLE IF EXISTS playlist CASCADE;
DROP TABLE IF EXISTS injuries CASCADE;
DROP TABLE IF EXISTS tracking CASCADE;

-- Creating tables
CREATE TABLE playlist (
	 playerkey INT ,
     gameid VARCHAR,
	 playkey VARCHAR,
	 rosterposition VARCHAR(50),
	 playerday INT,
	 playergame INT,
	 stadiumtype VARCHAR(50),
	 fieldtype  VARCHAR(50),
	 temperature INT,
	 weather VARCHAR(250),
	 playtype VARCHAR(50),
	 playergameplay INT,
	 position VARCHAR(50),
	 postiongroup VARCHAR(50),
	 PRIMARY KEY (playkey)
);



CREATE TABLE injuries (
     playerkey INT,
     gameid VARCHAR(50),
	 playkey VARCHAR(50) ,
	 bodypart VARCHAR(50),
	 fieldtype VARCHAR(50),
	 DM_M1 INT,
	 DM_M7 INT,
	 DM_M28 INT,
	 DM_M42 INT
);



CREATE TABLE tracking (
	 playkey VARCHAR(50),
	 tracking_time FLOAT ,
	 tracking_event VARCHAR(50) ,
	 x FLOAT ,
	 y FLOAT ,
	 dir FLOAT ,
	 dis FLOAT ,
	 o FLOAT ,
	 s FLOAT 
);