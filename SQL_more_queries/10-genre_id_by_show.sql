-- Import a database dump from hbtn_0d_tvshows to your MySQL server: download
SELECT tv_shows.title, tv_show_genre.genre_id FROM tv_shows
INNER JOIN tv_show_genres ON tv_show_genres.show_id
ORDER BY tv_show.title, tv_show_genres.genre_id;
