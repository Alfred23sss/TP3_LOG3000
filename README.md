# TP3 LOG3000 - Flask Calculator

## Project name
TP3 LOG3000 - Flask Calculator

## Team number
Team number: **[REPLACE_WITH_YOUR_TEAM_NUMBER]**

## Objective
This project delivers a simple web calculator built with Flask. The objective is to apply collaborative software engineering practices: documentation, testing, issue tracking, branch-based bug fixes, pull requests, and final validation.

## Project scope
- Backend arithmetic logic and expression parsing.
- Frontend calculator interface (HTML/CSS/JS).
- Automated tests to detect and prevent regressions.
- Traceable team workflow using GitHub issues and pull requests.

## Repository structure
- `TP3---LOG3000-main/`: application source code.
  - `app.py`: Flask entry point and route handling.
  - `operators.py`: arithmetic operations.
  - `templates/`: HTML templates.
  - `static/`: CSS assets.
  - `tests/`: test suite.

## Prerequisites
- Git
- Python 3.11+ and `pip`

## Installation guide
1. Clone the repository:
   - `git clone <REPOSITORY_URL>`
2. Move to the project folder:
   - `cd TP3_LOG3000/TP3---LOG3000-main`
3. Create a virtual environment:
   - Windows PowerShell: `python -m venv .venv`
4. Activate the environment:
   - Windows PowerShell: `.\\.venv\\Scripts\\Activate.ps1`
5. Install dependencies:
   - `python -m pip install --upgrade pip`
   - `python -m pip install flask pytest`

## Usage guide
1. Start the Flask app from `TP3---LOG3000-main`:
   - `python app.py`
2. Open your browser:
   - `http://127.0.0.1:5000/`
3. Use calculator buttons to compose an expression.
4. Press `=` to submit and display the result.

## Test guide
From `TP3---LOG3000-main` with virtual environment activated:
- Run all tests:
  - `pytest -q`
- Run a specific file:
  - `pytest -q tests/test_operators.py`

See `TP3---LOG3000-main/tests/README.md` for test coverage details.

## Contribution workflow
- Create or confirm a GitHub issue describing the bug/feature.
- Create a dedicated branch from main:
  - `fix/issue-<id>-short-description`
- Implement changes and add/update tests.
- Run tests locally before committing.
- Commit with a clear message focused on why the change is needed.
- Open a Pull Request linked to the issue.
- Review and merge after approval and passing tests.

## Notes for delivery
- Ensure all assignment sections are represented in repository history (issues, branches, PRs, tests, docs).
- Keep the repository public at deadline time and avoid post-deadline commits.