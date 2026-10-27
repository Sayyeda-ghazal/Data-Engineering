# #03 Backfill Idempotent Pipeline

**Difficulty:** Intermediate

## Problem

Design an Airflow DAG with catchup=True that can safely re-run for any historical date without duplicating data. Use an upsert strategy.

## Hints

- `INSERT ON CONFLICT DO UPDATE` in Postgres
- Partition data by `execution_date`

## Technologies

Airflow, PostgreSQL
