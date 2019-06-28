## Window Functions
# https://dev.mysql.com/doc/refman/8.0/en/window-functions-usage.html

Big problem is `GROUP BY` is you have to group ALL non-aggregated columns.
This means you can't compare an aggregated value to non-aggregated values.

Window functions can solve this issue. These are a class of functions that perform a calculation without grouping data.

Can generate the following Windows:
- OVER
- RANK

Key points:
- Windows are processed after the query except `ORDER BY`
- The window uses the results, rather than the database
- Can often be used in place of a subquery
- Unlike subquery, implements `WHERE` within the window because it works off the result query

### Window Partitions
`OVER` & `PARTITION BY`
- Calculate separate values for separate groups
- Calculate different calculations in the same columns
- Can partition by multiple columns

### Sliding Windows
- Row based calculations
- Calculates relative to current row of a dataset

```
ROWS BETWEEN <start> AND <finish>
```

Keywords for <start> and <finish>
Specify rows before and after current row
- PRECEDING
- FOLLOWING
Include all since begin 	or ending
- UNBOUNDED PRECEDING
- UNBOUNDED FOLLOWING
Stop calculations at current row
- CURRENT ROW


Some Code Examples:
USING OVER()
```
-- Simple OVER()
SELECT
	m.id, c.name AS country, m.season, m.home_goal, m.away_goal,
	AVG(m.home_goal + m.away_goal) OVER() AS overall_avg
FROM match AS m
LEFT JOIN country AS c ON m.country_id = c.id;
```

Using PARTITION BY, OVER

```
RANK() OVER (
    PARTITION BY <expression>[{,<expression>...}]
    ORDER BY <expression> [ASC|DESC], [{,<expression>...}]
)
```



```
SELECT
	date,
	season,
	home_goal,
	away_goal,
	CASE WHEN hometeam_id = 8673 THEN 'home'
         ELSE 'away' END AS warsaw_location,
    AVG(home_goal) OVER(PARTITION BY season,
         	EXTRACT(month FROM date)) AS season_mo_home,
    AVG(away_goal) OVER(PARTITION BY season,
            EXTRACT(month FROM date)) AS season_mo_away
FROM match
WHERE
	hometeam_id = 8673
    OR awayteam_id = 8673
ORDER BY (home_goal + away_goal) DESC;
```

Sliding Windows

```
SELECT
	date,
    home_goal,
    away_goal,
    SUM(home_goal) OVER(ORDER BY date DESC
         ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) AS running_total,
    AVG(home_goal) OVER(ORDER BY date DESC
         ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) AS running_avg
FROM match
WHERE
	awayteam_id = 9908
    AND season = '2011/2012';

```

```
select
name, weight,
min(weight) over (order by name ROWS between 1 preceding and 1 following)
from runners order by name
```

Running total of cats by breed and name.
```
SELECT name, breed, SUM(weight) OVER(PARTITION BY breed ORDER BY breed, name)
FROM cats
```
