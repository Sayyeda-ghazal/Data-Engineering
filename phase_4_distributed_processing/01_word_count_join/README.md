# #01 Word Count to Join

**Difficulty:** Beginner

## Problem

Start with Spark word count. Then progress: join two large DataFrames (users + events) efficiently. Identify if a broadcast join is possible and implement it.

## Hints

- `sc.textFile()` for RDD version
- `df.hint('broadcast')` for small tables

## Technologies

PySpark, Spark SQL
