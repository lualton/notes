
/* Get column names in table - two methods */
DESCRIBE table;

/* don't change column_name */
SELECT column_name
FROM information_schema.columns
WHERE table_name='table'



/* Select entire table */
SELECT *
FROM table;

/* Select columns from table */
SELECT column1, column2, columnN
FROM table;

/* Get Unique values */
SELECT DISTINCT column1
FROM table;

/* Get Number of Rows in one or more columns */
SELECT COUNT(*)
FROM table;

/* Get Number of Unique Values in column */
SELECT COUNT(DISTINCT column1)
FROM table;

/* Filtering ------------------------- */
SELECT *
FROM table
WHERE column1 > xxx
/* =, <>, <, >, <=, >= */

SELECT *
FROM table
WHERE column1 = 'some-text'

/* filter multiple */
SELECT *
FROM table
WHERE column1 = condition
AND column1 = other_condition

/* Using Or */
SELECT *
FROM table
WHERE (column1 = xxx OR column1 = yyy)
AND (column2 = 'text' OR column2 = 'more-text');

/* Find a range (between) */
SELECT *
FROM table
WHERE column1 BETWEEN x AND y

/* NULL */
SELECT *
FROM table
WHERE column1 IS NULL
AND column2 IS NOT NULL

/* LIKE */
SELECT *
FROM table
WHERE column1 LIKE 'A%'
AND column2 NOT LIKE '_A%'
/* % - any text standin; _ for any before characters */


/* IN */
WHERE column IN (x, y)
WHERE column NOT IN (x, y)


/* Aggregate */
SELECT SUM(column1)
SELECT AVG(column1)
SELECT MIN(column1)
SELECT MAX(column1)

/* Alias */
SELECT column AS name
SELECT column1 - column2 AS name

/* Order by, ordering, sorting */
SELECT column
FROM table
ORDER BY column DESC

/* Grouping */
SELECT column
FROM table
GROUP BY column;

SELECT column
FROM table
WHERE
GROUP BY
HAVING AGG(column)
ORDER BY
