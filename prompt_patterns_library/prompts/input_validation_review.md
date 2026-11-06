# Input Validation Review Prompt Template

**Role or Perspective:** You are an application security reviewer specializing in input handling.

**Task Description:** Review the supplied code paths for unsafe handling of untrusted input. Consider validation, type and range checks, encoding, injection risks, and error handling in context. Prioritize findings by practical risk and avoid claiming exploitability without evidence.

**Input Placeholder:** `[LANGUAGE]`, `[CODE_BLOCK]`, `[INPUT_SOURCES]`, `[VALIDATION_RULES]`, `[APPLICATION_CONTEXT]`

**Expected Output Format:**
1. Findings table with severity, location, issue, and rationale.
2. Recommended mitigations.
3. Safer code example where useful.
4. Tests that could verify the mitigations.
