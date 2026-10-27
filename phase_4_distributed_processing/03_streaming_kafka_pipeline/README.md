# #03 Streaming Kafka Pipeline

**Difficulty:** Advanced

## Problem

Set up a local Kafka cluster. Produce clickstream events. Write a Spark Structured Streaming job that aggregates clicks per product per minute and writes to PostgreSQL.

## Hints

- Use `kafka-python` or `confluent-kafka`
- `foreachBatch()` sink for Postgres writes

## Technologies

Kafka, PySpark, Structured Streaming, PostgreSQL
