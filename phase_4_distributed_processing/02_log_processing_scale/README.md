# #02 Log Processing at Scale

**Difficulty:** Intermediate

## Problem

Process 50M web server log lines with PySpark. Extract status codes, parse timestamps, compute p50/p95/p99 response times per endpoint per day.

## Hints

- Use `regexp_extract` for parsing
- `percentile_approx()` for percentiles

## Technologies

PySpark, Spark SQL
