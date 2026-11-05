# API Scenario Runner

A dependency-free offline assertion runner for **recorded** HTTP response data. Compare status codes and selected JSON body/header fields against expectations.

## Run

```bash
python app.py examples/cases.json
python -m unittest discover -s tests -v
```

Input is a JSON array of cases containing `name`, `actual` and `expected`. Only expected fields are checked. Exit code 0 means all cases passed, 1 means failed assertions, and 2 means malformed input.

## Scope

This tool does **not** make live HTTP requests. It is intended for repeatable fixture-based API contract tests.
