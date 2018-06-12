CREATE USER postgres_user WITH PASSWORD 'password';
CREATE DATABASE my_postgres_db OWNER postgres_user;
SET ROLE postgres_user;
DROP TABLE IF EXISTS tweets;
CREATE TABLE tweets(
   id serial PRIMARY KEY,
   screenname varchar (40) NOT NULL,
   text varchar (500) NOT NULL,
   lang varchar (10) NOT NULL,
   created_at DATE
);
