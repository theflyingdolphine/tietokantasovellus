CREATE TABLE users (
	id SERIAL PRIMARY KEY, 
	username TEXT, 
	password TEXT,
	role INT
);

CREATE TABLE game1 (
	id SERIAL PRIMARY KEY,
	content TEXT
);

CREATE TABLE game2 (
	id SERIAL PRIMARY KEY,
	content TEXT
);

CREATE TABLE game3 (
	id SERIAL PRIMARY KEY,
	creator INT,
	question TEXT,
	answer INT
);

INSERT INTO game3 (question, answer) VALUES ('What is 2 to the power of 5', 32);

CREATE TABLE reviews (
	id SERIAL PRIMARY KEY,
	content TEXT
);

CREATE TABLE statistics (
	id SERIAL PRIMARY KEY,
	username TEXT,
	game1 INT,
	game2 INT,
	other INT
);
