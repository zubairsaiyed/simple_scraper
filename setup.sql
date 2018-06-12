CREATE DATABASE IF NOT EXISTS my_insight_project;
DROP TABLE IF EXISTS my_insight_project.tweets;
CREATE TABLE my_insight_project.tweets(
   id INT NOT NULL AUTO_INCREMENT,
   screenname VARCHAR(40) NOT NULL,
   text VARCHAR(500) NOT NULL,
   created_at DATE,
   PRIMARY KEY ( id )
);
