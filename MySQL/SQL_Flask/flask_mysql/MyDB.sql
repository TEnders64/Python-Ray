ALTER Table mydb.users ADD COLUMN name VARCHAR(128) AFTER id;
INSERT INTO `mydb`.`users` (`name`, `email`, `password`) VALUES ('Phred', 'pm@hotmail.com', 'pmRocks');
SELECT * FROM mydb.users;
INSERT INTO `mydb`.`users` (`name`, `email`, `password`) VALUES ('Aloysuis', 'BigA@gmail.com', 'AAAAAA');
INSERT INTO `mydb`.`users` (`name`, `email`, `password`) VALUES ('Joan', 'JoanofArc@eu.com', 'Save The World');
