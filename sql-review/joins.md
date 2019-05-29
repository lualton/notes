
## Quick Joins Notes
https://www.dofactory.com/sql/join


## Thinking about cases and examples

#### Semi Joins
Assume we're a Bank:
  - Table A: Customer Data [ID, Phone, Address, Credit Score]
  - Table B: Credit Card Data [ID, start, end, product_type, balance]

1. We want all the customer ID's that have product_type A and a balance below $2000. The Bank wants to use these customers later for some promotion or referral program.
2. Subquery table B for ID's WHERE product_type = A and Balance <= $2000.
3. Main query ID from Table A, using WHERE EXISTS to filter with subquery

```
SELECT ID
FROM tableA
WHERE EXISTS (SELECT ID
              FROM tableB
              WHERE product_type = 'A'
              AND balance <= 2000);
```
