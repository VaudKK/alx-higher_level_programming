-- Number by score

SELECT score, COUNT(*) AS number GROUP BY score ORDER by score DESC;
