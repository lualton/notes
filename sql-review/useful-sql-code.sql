/*
Contains code chunks for useful SQL code
*/


-- Regular Expression, Finding rows based on some codition

-- Finds city names starting with a vowel
SELECT DISTINCT city
FROM station
WHERE city REGEXP "^[aeiou].*";
--.*[aeiou]$ for ending with a vowel

-- City names that do not contain vowels regexp
SELECT DISTINCT City
FROM Station
WHERE City REGEXP '[^aeiou]$';

-- Substring, get part of a string
-- Subsets from 1st position to 3rd position
SELECT substr(column, 1, 3)

-- Gets the last two characters
SELECT substr(column, -2)

-- Column equals multiple values
WHERE column IN (1,2,3,4,5)

SELECT name, continent
FROM world
WHERE continent IN (
  SELECT continent
  FROM world
  WHERE name IN ('Argentina', 'Australia'));


-- Get Top N
SELECT TOP 5 salary
-- If you want to get top 3rd
SELECT TOP 1 salary
FROM (SELECT TOP 3 salary, FROM employee ORDER BY salary DESC)


-- Similar Rows in Two Tables
INTERSECT

-- Query based on row number
WHERE rowno = 2
WHERE mod(rowno, 2) = 0 -- for even rows
