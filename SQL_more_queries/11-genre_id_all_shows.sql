-- Lists all shows in database hbtn_0d_tvshows, if not a show display NULL.
-- ASCENDING ORDER tv_shows.title and tv_show_genres.genre_id.
SELECT i.`title`, n.`genre_id` FROM `tv_shows` AS i
LEFT JOIN `tv_show_genres` AS n
ON i.`id` = n.`show_id` ORDER BY i.`title`, n.`genre_id`; 