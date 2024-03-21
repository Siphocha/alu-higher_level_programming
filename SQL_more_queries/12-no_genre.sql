-- Same as Q11 but no need for NUll statements.
SELECT i.`title`, n.`genre_id`
  FROM `tv_shows` AS i
       LEFT JOIN `tv_show_genres` AS n
       ON i.`id` = n.`show_id`
       WHERE n.`genre_id` IS NULL
 ORDER BY i.`title`, n.`genre_id`;