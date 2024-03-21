-- Lists all genres of the show Dexter in hbtn_0d_tvshows. Records ordered in ASCENDING ORDER.
SELECT i.`name`
  FROM `tv_genres` AS i
       INNER JOIN `tv_show_genres` AS n
       ON i.`id` = n.`genre_id`

       INNER JOIN `tv_shows` AS p
       ON p.`id` = n.`show_id`
       WHERE p.`title` = "Dexter"
 ORDER BY i.`name`;