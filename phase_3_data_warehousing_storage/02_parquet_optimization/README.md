# #02 Parquet Optimization

**Difficulty:** Intermediate

## Problem

Take a 5GB CSV file. Convert it to Parquet with optimal partitioning by year/month. Compare query times in DuckDB for a date-range filter query before and after.

## Hints

- Use `pyarrow` or `pandas to_parquet()`
- Measure with `%timeit` or `time` module

## Technologies

Parquet, DuckDB, Python
