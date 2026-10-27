# #03 SCD Type 2 in dbt

**Difficulty:** Advanced

## Problem

Model a customer address table as SCD Type 2 using dbt snapshots. When a customer updates their city, the old record should be closed with an end_date and a new record opened.

## Hints

- Use dbt snapshot with `strategy: timestamp`
- `check_cols: ['city', 'state']`

## Technologies

dbt, SQL
