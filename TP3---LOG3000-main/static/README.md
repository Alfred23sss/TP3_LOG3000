# Static Assets Module

## Purpose
This directory contains static frontend assets served by Flask.

## Main files
- `style.css`: Visual layout and styling rules for the calculator interface.

## Dependencies and assumptions
- Referenced by `templates/index.html` via `url_for('static', filename='style.css')`.
- Assumes modern browser support for CSS Grid and basic transitions.
