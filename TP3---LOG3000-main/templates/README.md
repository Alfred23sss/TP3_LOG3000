# Templates Module

## Purpose
This directory contains Jinja2 HTML templates used by the Flask app to render pages.

## Main files
- `index.html`: Main calculator page; includes display input, buttons, and client-side helper JavaScript.

## Dependencies and assumptions
- Rendered by Flask's `render_template`.
- Expects a `result` template variable from the backend.
- Uses static CSS from `../static/style.css`.
