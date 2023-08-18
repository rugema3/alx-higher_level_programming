-- Create Database and user at the same time.


-- First create the database.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- select the database.
USE hbtn_0d_2;

-- Now created a user in that database and grant previlegdes.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- grant priviledges.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
