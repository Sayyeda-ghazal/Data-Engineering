# #04 Delta Lake ACID Pipeline

**Difficulty:** Advanced

## Problem

Build a medallion pipeline on Delta Lake: raw JSON -> Bronze (append-only) -> Silver (deduped, typed) -> Gold (aggregated). Use MERGE for upserts in Silver.

## Hints

- `delta.tables.DeltaTable.forPath()`
- `MERGE INTO` with matched/not matched

## Technologies

Delta Lake, PySpark
