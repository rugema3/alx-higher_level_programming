-- List all shows and their linked genres

-- Use the query to get the desired output
SELECT
    tv_shows.title,
    tv_genres.name AS genre
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, genre ASC;
