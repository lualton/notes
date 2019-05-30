
## Order of Execution

Start with full database of data

1. FROM - restrict results to the tables
2. WHERE - filter specific rows
3. GROUP BY - grouping
4. HAVING - filter out groups
5. SELECT - choose columns
6. ORDER - order the rows in the columns chosen

General big picture of execution order
- Begins with tables
- Next are row operations
- Then column operations
- Then sorting


## Types of Joins
- Inner Join: Set that matches in both table A and table B
- Self Join: Set A to Set A.
- Outer Joins
  - Full: Set that matches all records in table A and table B + Null for non-matching records
  - Left Join: Table A + Matching records from Table B. Null if no matching records
  - Right Join: Table B + Matching Records or Null from Table A.
- Cross Join (Cartesian Product): Joins Everything to Everything. Table A = 10, Table B = 10, Joined Table = 100

These joins are similar to filtering or WHERE clause
- Semi Join: Rows in Table A that EXIST in Table B, but doesn't actually join. This acts as a constraint where we only want rows of Table A that are present in Table B.
- Anti Join: Useful in identifying which records are causing an incorrect number of records to appear in join queries. Table A - Table B. Returns rows in Table A that are not present in Table B. This is the opposite of a semi-join.

## Joins vs Unions

Joins work on columns while Unions combine rows.
Joins typically make a table wider while unions make it taller.

## Unions (Set Theory)
- UNION - includes rows from Set A and Set B, but no duplicates
- UNION ALL - include rows from Set A and Set B with duplicates
- INTERSECT - only includes rows in common between Set A and Set B
- EXCEPT - include rows in Set A that are not in Set B


## Subqueries

- Can be used in any part of query
- Return a variety of information (scalars, lists)
- Can return another table

- Use to compare groups to summarized values
  - Find how one group performance compared to the average across all groups.
  - How well did product A sell compared to all products
  - Which student groups performed above average?
- Reshape Data
  - What is the highest monthly average product sold in region A.
- Combine Data that usually can't be joined

## Correlated Subqueries
Normal Subqueries:
- Run independently of the main query
- Evaluated once with whole query

Correlated:
- Dependent on main query
- Evaluated in loops

You can often use correlated subqueries instead of joins

Correlated subqueries are basically loops in SQL, written in reverse, with condition as WHERE




## Common Table Expression

Special Subquery declared ahead of main query

```
WITH cte AS (
        SELECT x
        FROM y )

SELECT x
FROM cte
```

Using `WITH name` will create the common table expressions

Benefits
- Executes once
- Improves query performance
- Improves organization of query
- Can reference itself

## Technique Differences

Joins
- Combine 2 tables
- Simple aggregations

- What is total sales per employee?


Correlated Subqueries
- Match subqueries and joins
- Allows more complicated expressions that joins can't
- High processing time

- Useful for matching data from different columns within one or more tables
- Who does each employee report to?

Multiple/Nested Subqueries
- Useful for step-by-step transformations of data
- Break down steps

- What is the average deal size closed by each sales rep in the quarter?

Common Table Expressions
- Allows organization of subqueries
- Basically the same as functions
- Only need to run it once for long queries or for multiple use

- Useful for comparing a lot of tables
- How did sales, growth, engineering teams perform on KPI's last year?

## DATES

If a date column:

`month FROM date`
