# Regression Investigation Prompt Template

**Role or Perspective:** You are a software engineer investigating a regression.

**Task Description:** Compare the previously working behavior with the current failure. Use the supplied changes to identify likely causes and suggest a focused way to reproduce and fix the problem.

**Input Placeholder:** `[FAILING_BEHAVIOR]`, `[RECENT_CHANGES_OR_DIFF]`, `[KNOWN_GOOD_VERSION]`, `[ENVIRONMENT]`

**Expected Output Format:**
1. Candidate change(s) that may have caused the regression.
2. Reasoning and evidence for each candidate.
3. Minimal reproduction steps.
4. Suggested fix and regression test.
