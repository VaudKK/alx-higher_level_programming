-- Genre ID by show

SELECT name, COUNT(tv_show_genres.genre_id) AS number_of_shows FROM tv_genres
INNER JOIN tv_show_genres
ON id = tv_show_genres.genre_id
GROUP BY name
ORDER BY number_of_shows DESC;
