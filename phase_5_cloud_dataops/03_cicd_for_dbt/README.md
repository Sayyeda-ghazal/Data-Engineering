# #03 CI/CD for dbt

**Difficulty:** Advanced

## Problem

Set up a GitHub Actions workflow that: runs dbt compile on PR, runs dbt test on merge to main, and posts test results as a PR comment.

## Hints

- Use `dbt-action` or custom python step
- `dbt source freshness` + `dbt test --select state:modified`

## Technologies

GitHub Actions, dbt, CI/CD
