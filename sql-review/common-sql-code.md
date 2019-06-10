

#### Keyword ALL to act over list
We want to filter based on population being greater than the rest of the population.
Normally, we'd think to do something similar to:
WHERE population >= MAX(population),
but we can't do aggregates in the where clause
```
SELECT name
  FROM world
 WHERE population >= ALL(SELECT population
                           FROM world
                          WHERE population>0)
```
