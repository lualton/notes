/*
Subqueries are a query nested inside another query
Used for intermediate transformations
- Creating a query off another query
- The subquery is treated as a new table that the main query uses
*/


-- Subqueries in WHERE
-- Useful for filtering results based on calculated information
-- Filter wiht a single scalar or a list with IN

SELECT AVG(test_score_math), AVG(test_score_read)
FROM student
WHERE AVG(test_score_math) * 2 >
    (SELECT AVG(test_score_math)
      FROM student)
GROUP BY demographics;

-- Subqueries in FROM
-- Useful to restructure and transform your data
-- Reshape, pre filter, before calculations
-- Calculating aggregates of aggregates
-- NOTE: Make sure to alias and join

SELECT team, home_avg
FROM (SELECT
    t.team_long_name AS team,
    AVG(m.home_goal) AS home_avg
FROM match AS m
    LEFT JOIN team AS t
        ON m.hometeam_id = t.team_api_id
WHERE season = '2011/2012'
GROUP BY team) AS subquery


-- Subqueries in SELECT
-- Used to return a single aggregate value (cannot normally include agg in ungrouped query)
-- Useful for mathematical (standard deviation of performance of group of students on a test)
-- Must return a single value or else error
-- Make sure to filter properly in both queries when in SELECT
SELECT date,
  (home_goal + away_goal) AS goals,
  (home_goal + away_goal) - 2.72 AS diff
FROM match
WHERE season = '2011/2012';

/*
Best practices:
- Can include many subqueries
- Make sure you filter properly in each subquery and main query
- Ask whether this subquery is actually necessary
- Annotate complex queries

*/
