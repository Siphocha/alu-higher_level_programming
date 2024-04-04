-- THis sript tracks num of occurences of particular scores grouped by score.
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;