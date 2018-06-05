CREATE DATABASE  IF NOT EXISTS TheWall; 
USE TheWall;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id  int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
	first_name varchar(255) DEFAULT NULL,
	last_name  varchar(255) DEFAULT NULL,
	email      varchar(255) DEFAULT NULL,
	password   varchar(255) DEFAULT NULL,
	created_at datetime DEFAULT NULL,
	updated_at datetime DEFAULT NULL
);

DROP TABLE IF EXISTS messages;
CREATE TABLE messages (
	id  int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
	user_id int(11) DEFAULT NULL,
	content TEXT DEFAULT NULL,
	created_at datetime DEFAULT NULL,
	updated_at datetime DEFAULT NULL
);

DROP TABLE IF EXISTS comments;
CREATE TABLE comments (
	id  int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
	user_id int(11) DEFAULT NULL,
	message_id int(11) DEFAULT NULL,
	comment TEXT DEFAULT NULL,
	created_at datetime DEFAULT NULL,
	updated_at datetime DEFAULT NULL
);


/* Assumes every message has a different created_at - Need a UNIQUE Key on created_at
SELECT user_id, id AS message_id, created_at AS message_date, content, "message" AS type FROM messages
	UNION
SELECT user_id, message_id,  
	(SELECT created_at FROM messages WHERE messages.id  = comments.message_id ) AS message_date, comment, "comment" AS type FROM comments
	ORDER BY message_date, type DESC;

SELECT user_id, message_id,  
	(SELECT created_at FROM messages WHERE messages.id  = comments.message_id ) AS message_date
	FROM comments;

collate utf8_general_ci

SELECT id, user_id, content FROM messages;
SELECT  id, user_id, message_id, comment FROM comments;