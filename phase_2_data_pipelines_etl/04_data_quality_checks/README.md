# #04 Data Quality Checks

**Difficulty:** Advanced

## Problem

Add Great Expectations checkpoints to a pipeline that validates: row counts didn't drop >10%, no nulls in primary keys, revenue column is always positive.

## Hints

- `ExpectationSuite` + `Checkpoint` API
- Fail pipeline on validation failure

## Technologies

Great Expectations, Python
