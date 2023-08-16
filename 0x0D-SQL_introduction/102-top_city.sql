-- Display the top 3 cities' temperatures during July and 
-- August ordered by temperature (descending)

SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8  -- Selects records from July and August
GROUP BY city  -- Grouping by city
ORDER BY avg_temp DESC -- Ordering by average temperature
LIMIT 3;

