# Tests Module

## Purpose
This directory contains automated tests for the calculator backend logic and key Flask route behavior.

## Coverage
- `test_operators.py`:
  - verifies arithmetic correctness for `add`, `subtract`, `multiply`, `divide`
  - verifies error behavior for division by zero
- `test_app.py`:
  - verifies expression parsing and validation in `calculate`
  - verifies `POST /` result rendering
  - verifies calculator UI button labels expected by users

## How to run
From `TP3---LOG3000-main` with the virtual environment activated:
- Run all tests: `pytest -q`
- Run operator tests only: `pytest -q tests/test_operators.py`
- Run app tests only: `pytest -q tests/test_app.py`

## Notes
Some tests are intentionally expected to fail before bug fixes are applied. These failures are used to open and track GitHub issues before implementing corrections.
