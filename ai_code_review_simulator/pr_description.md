# Pull Request: Add Python Code Review Simulator

## Summary
Add a lightweight static code review simulator that identifies common Python code quality issues and produces a readable review report.

## Changes
- Added `code_review.py` with Python syntax validation.
- Added checks for long lines, debug print statements, bare exception handlers, short function names, and missing docstrings.
- Added finding summaries grouped by severity: ERROR, WARNING, and INFO.
- Added a readable text report formatter.
- Added `test_code_review.py` with unit tests for the main review checks and report generation.

## Context
This feature provides an initial automated review capability for the AI Code Review Simulator project. It helps developers identify common code quality problems before submitting changes.

## Testing
Run the unit tests with:

```bash
python -m unittest -v
```

## Scope
This is a lightweight static analysis feature. It does not replace a full linter or an AI-powered code review service.
