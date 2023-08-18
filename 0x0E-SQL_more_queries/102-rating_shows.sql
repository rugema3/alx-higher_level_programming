-- List all shows by their rating sum using a RIGHT JOIN
SELECT
    tv_shows.title,
    SUM(tv_show_ratings.rate) AS rating
FROM tv_show_ratings
RIGHT JOIN tv_shows ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating DESC;
