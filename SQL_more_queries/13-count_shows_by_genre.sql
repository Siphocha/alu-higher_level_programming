-- Lists all genres from database hbtn_0d_tvshows with num of links of each.
-- No genres if no links, going by DESCENDING order
SELECT i.`name` AS `genre`, COUNT(*) AS `number_of_shows`
FROM `tv_genres` AS i INNER JOIN `tv_show_genres` AS n ON i.`id` = n.`genre_id`
GROUP BY i.`name` ORDER BY `number_of_shows` DESC;
