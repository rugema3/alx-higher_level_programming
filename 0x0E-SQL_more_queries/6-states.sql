-- A script that creates the database hbtn_0d_usa and the table states
-- (in the database hbtn_0d_usa) on your MySQL server.

-- First create the DATABASE
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database where you want the table to be created.
USE hbtn_0d_usa;

-- Now create the table in the selected database.
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
	);

