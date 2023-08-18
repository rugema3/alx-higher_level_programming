-- A script that creates the database hbtn_0d_usa and the table cities 
-- (in the database hbtn_0d_usa) on your MySQL server.

-- Create the database hbtn_0d_usa if it doen't exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database to work with.
USE hbtn_0d_usa;

-- Create a table cities in the selected db.
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
	);
