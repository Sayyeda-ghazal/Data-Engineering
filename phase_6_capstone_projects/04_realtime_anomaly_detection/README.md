# #04 Real-time Anomaly Detection

**Difficulty:** Expert

## Problem

Stream sensor/metric data through Kafka. Use Spark Streaming + a simple statistical model (z-score or IQR) to detect anomalies in real-time. Alert via Slack webhook when anomaly detected.

## Hints

- Rolling window statistics with watermarks
- `requests` library for Slack webhook

## Technologies

Kafka, Spark Streaming, Python, Slack API
