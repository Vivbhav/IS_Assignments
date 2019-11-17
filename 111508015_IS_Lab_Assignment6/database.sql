DROP DATABASE injection;
CREATE DATABASE injection;
USE injection;
DROP table IF EXISTS users;
create table users (
	user_id int, 
	username varchar(100),
	random_num int,
	password varchar(255)
);
insert into users values (1, 'vivek', 21, 'bhave'); 
insert into users values (2, 'chinmay', 211, 'bahulikar');
insert into users values (3, 'ankush', 107, 'karmarkar');
insert into users values (4, 'jaee', 45, 'm');
insert into users values (5, 'isha', 29, 'j');
insert into users values (6, 'sushrut', 121, 'a');
insert into users values (7, 'sayali', 23, 'n');
