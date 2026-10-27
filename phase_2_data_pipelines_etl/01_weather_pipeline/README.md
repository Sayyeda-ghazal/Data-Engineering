# #01 Weather Pipeline

**Difficulty:** Beginner

## Problem

Build an Airflow DAG that fetches weather data from OpenWeatherMap API every 6 hours, stores raw JSON in a local folder, and loads parsed data into PostgreSQL.

## Hints

- Use `SimpleHttpOperator` or `PythonOperator`
- Store raw + processed separately

## Technologies

Airflow, REST APIs, PostgreSQL
