-- A script that creates the table id_not_null on MYSQL SERVER./

-- Create the table with a default value.
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
	);
