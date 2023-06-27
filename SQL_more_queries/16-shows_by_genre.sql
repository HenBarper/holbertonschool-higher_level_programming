-- Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv_shows.title AS title, tv_genres.name AS name
FROM tv_shows

GROUP BY tv_shows.title, tv_genres.name;