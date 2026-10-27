# #01 Streaming E-Commerce Analytics

**Difficulty:** Advanced

## Problem

Build end-to-end: Kafka produces fake e-commerce events -> Spark Structured Streaming aggregates -> Delta Lake stores -> dbt transforms -> Grafana visualizes orders per minute, revenue, top products.

## Hints

- Use `faker` library for event generation
- Grafana + Delta Lake via Trino connector

## Technologies

Kafka, PySpark, Delta Lake, dbt, Grafana, Trino
