-- lists all genres of the show Dexter.
SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_show_genres.shoq_id = tv_shows.id WHERE tv_shows.tittle = 'Dexter'
GROUP BY name ORDER BY name ASC;
