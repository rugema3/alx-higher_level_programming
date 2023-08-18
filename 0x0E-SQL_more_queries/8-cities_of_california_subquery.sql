-- A script that lists all the cities of California that can be found in the database hbtn_0d_usa.

-- Find the state's id for California
SELECT id INTO @california_id FROM states WHERE name = 'California';

-- List all cities of California and sort by cities.id
SELECT id, name
FROM cities
WHERE state_id = @california_id
ORDER BY id ASC;
