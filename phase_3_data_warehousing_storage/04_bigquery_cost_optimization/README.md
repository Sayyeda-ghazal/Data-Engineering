# #04 BigQuery Cost Optimization

**Difficulty:** Advanced

## Problem

Given a 1TB table queried daily, implement partitioning by date and clustering by customer_id. Write 3 sample queries and explain how the partition pruning reduces bytes scanned.

## Hints

- `PARTITION BY DATE(_PARTITIONTIME)`
- `CLUSTER BY` reduces sort scan

## Technologies

BigQuery, SQL
