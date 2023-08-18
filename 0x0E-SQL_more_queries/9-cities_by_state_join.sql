-- Listing all cities in the database.

-- List all cities and their corresponding state names
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
LEFT JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
