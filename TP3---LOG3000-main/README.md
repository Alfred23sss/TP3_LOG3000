# Calculator Application Module

## Purpose
This module contains the runnable Flask calculator application, including backend arithmetic logic and frontend assets.

## Main files
- `app.py`: Flask app entry point, request handling, expression parsing, and result rendering.
- `operators.py`: Arithmetic operations used by the calculator.
- `templates/index.html`: User interface for entering expressions and submitting calculations.
- `static/style.css`: Styling for the calculator page.

## Dependencies and assumptions
- Python 3.11+.
- Flask runtime dependency.
- Assumes simple two-operand expressions with exactly one operator (`+`, `-`, `*`, `/`).
