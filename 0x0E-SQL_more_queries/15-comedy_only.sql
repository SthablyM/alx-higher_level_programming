--  lists all Comedy shows in the database hbtn_0d_tvshows.
value
SELECT tittle
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows_genres.genres_id = tv_show_genres.id
WHERE tv_genres.name = 'comedy'
GROUP BY title
ORDER BY title ASC;
