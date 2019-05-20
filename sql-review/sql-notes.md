
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


## Joins
- Inner Join: Set that matches in both table A and table B
- Outer Joins
  - Full Outer: Set that matches all records in table A and table B + Null for non-matching records
  - Left Join: Table A + Matching records from Table B. Null if no matching records
  - Right Join: Table B + Matching Records or Null from Table A.
- Cross Join (Cartesian Product): Joins Everything to Everything. Table A = 10, Table B = 10, Joined Table = 100 
