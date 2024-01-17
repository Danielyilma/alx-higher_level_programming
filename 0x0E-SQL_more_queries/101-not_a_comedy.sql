-- join with sub query
SELECT DISTINCT tv_shows.title
FROM
tv_shows LEFT OUTER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.id NOT IN (
    SELECT tv_show_genres.show_id
    FROM
    tv_genres INNER JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title;
