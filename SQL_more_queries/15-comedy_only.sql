-- Lists all comedy shows in database hbtn_0d_tvshows. DESCENDING ORDER by show title.
SELECT i.`title`
  FROM `tv_shows` AS i
       INNER JOIN `tv_show_genres` AS n
       ON i.`id` = n.`show_id`

       INNER JOIN `tv_genres` AS p
       ON p.`id` = n.`genre_id`
       WHERE p.`name` = "Comedy"
 ORDER BY i.`title`;