
-- CASE is a SQL if statement


-- Renaming columns into 3 buckets, and group by those buckets
-- Allows grouping within a single column without a join
SELECT
	CASE WHEN column1 = condition1 THEN 'Something 1'
         WHEN column1 = condition2 THEN 'Something 2'
         ELSE 'Something 3' END
         AS alias1,
FROM table1
GROUP BY alias1;

-- Comparisons between columns
SELECT
	column1,
	CASE WHEN column2 > column3 THEN 'Something 1'
        ELSE 'Something 2' END AS alias1
FROM table1;

-- Using CASE within a WHERE statement as a filtering mechanism
SELECT season, date, home_goal, away_goal
FROM matches_italy
WHERE
	CASE WHEN hometeam_id = 9857 AND home_goal > away_goal THEN 'Bologna Win'
         WHEN awayteam_id = 9857 AND away_goal > home_goal THEN 'Bologna Win'
         END IS NOT NULL;

-- Counting
-- SQL can't sum TRUE/FALSE, so convert to 1/0
SELECT
	c.name AS country,
   -- Sum the total records in each season where the home team won
	SUM(CASE WHEN m.season = '2012/2013' AND m.home_goal > m.away_goal
       THEN 1 ELSE 0 END) AS matches_2012_2013,
	SUM(CASE WHEN m.season = '2013/2014' AND m.home_goal > m.away_goal
       THEN 1 ELSE 0 END) AS matches_2013_2014,
	SUM(CASE WHEN m.season = '2014/2015' AND m.home_goal > m.away_goal
       THEN 1 ELSE 0 END) AS matches_2014_2015
FROM country AS c
LEFT JOIN match AS m
ON c.id = m.country_id
-- Group by country name alias
GROUP BY country;

-- Taking a percent and rounding
SELECT
	c.name AS country,
    -- Round the percentage of tied games to 2 decimal points
	ROUND(AVG(CASE WHEN m.season='2013/2014' AND m.home_goal = m.away_goal THEN 1
			 WHEN m.season='2013/2014' AND m.home_goal != m.away_goal THEN 0
			 END),2) AS pct_ties_2013_2014,
	ROUND(AVG(CASE WHEN m.season='2014/2015' AND m.home_goal = m.away_goal THEN 1
			 WHEN m.season='2014/2015' AND m.home_goal != m.away_goal THEN 0
			 END),2) AS pct_ties_2014_2015
FROM country AS c
LEFT JOIN matches AS m
ON c.id = m.country_id
GROUP BY country;
