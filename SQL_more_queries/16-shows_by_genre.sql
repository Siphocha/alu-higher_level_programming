-- Lists all shows and genres from hbtn_0d_tvshows. ASCENDING ORDER show title and genre name.
SELECT i.`title`, n.`name`
  FROM `tv_shows` AS i
       LEFT JOIN `tv_show_genres` AS p
       ON i.`id` = p.`show_id`

       LEFT JOIN `tv_genres` AS n
       ON p.`genre_id` = n.`id`
 ORDER BY i.`title`, n.`name`;