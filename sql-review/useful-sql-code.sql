/*
Contains code chunks for useful SQL code
*/


-- Regular Expression, Finding rows based on some codition

-- Finds city names starting with a vowel
SELECT DISTINCT city
FROM station
WHERE city REGEXP "^[aeiou].*";
--.*[aeiou]$ for ending with a vowel
