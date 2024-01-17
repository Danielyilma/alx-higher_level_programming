-- list all genre
SELECT DISTINCT tv_genres.name
FROM
tv_genres LEFT OUTER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.id NOT IN (
    SELECT tv_show_genres.genre_id
    FROM tv_shows INNER JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name;
