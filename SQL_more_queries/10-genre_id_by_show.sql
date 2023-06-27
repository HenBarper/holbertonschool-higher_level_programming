-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN states ON cities.state_id = states.id