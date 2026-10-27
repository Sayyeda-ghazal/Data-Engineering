# #02 SQL Window Functions Challenge

**Difficulty:** Beginner

## Problem

Given an orders table (order_id, customer_id, amount, date), write a query to find the top 3 orders per customer using window functions.

## Hints

- `ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount DESC)`

## Technologies

SQL, PostgreSQL
