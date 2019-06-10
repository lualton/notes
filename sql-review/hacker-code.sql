-- SELECT *, CASE WHEN p2.start_date IS NULL THEN 1
--             ELSE 0 END AS project_break
-- FROM projects AS p1
-- LEFT JOIN projects AS p2
-- ON p1.end_date = p2.start_date
-- ORDER BY p1.start_date;
SELECT *
FROM
    (SELECT start_date
    FROM projects
    WHERE start_date NOT IN (SELECT end_date FROM projects)) AS p1,
    (SELECT end_date
    FROM projects
    WHERE end_date NOT IN (SELECT start_date FROM projects)) AS p2
WHERE p1.start_date < p2.end_date;



SELECT end_date
FROM projects
WHERE end_date NOT IN (SELECT start_date FROM projects))
