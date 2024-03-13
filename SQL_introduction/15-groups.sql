-- Script that lists the number of records eith the same score in the table
SELECT score, COUNT (score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
