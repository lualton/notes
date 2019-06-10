
Normal Subqueries:
Run independently of the main query
Evaluated once with whole query

Correlated:
Dependent on main query
Evaluated in loops

You can often use correlated subqueries instead of joins

correlated subqueries are basically loops
in SQL, written in reverse, with condition as WHERE


```
-- Selecting information from separate tables
SELECT  c.company_code,c.founder,
  (SELECT count(*) FROM Lead_Manager WHERE company_code=c.company_code ) ,
  (SELECT count(*) FROM Senior_Manager WHERE company_code=c.company_code ),
  (SELECT count(*) FROM Manager WHERE company_code=c.company_code ),
  (SELECT count(*) FROM Employee  WHERE company_code=c.company_code )
FROM  Company AS c
ORDER BY c.company_code;
```
