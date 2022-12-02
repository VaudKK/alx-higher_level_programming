-- Genre ID by show

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genre ON tv_shows.id = tv_show_genre.show_id;
