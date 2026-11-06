# Regression Test Creation Prompt Template

**Role or Perspective:** You are a test automation engineer preventing previously fixed defects from returning.

**Task Description:** Turn the supplied bug report and fix into a focused regression test. The test should fail against the buggy behavior and pass when the fix is applied.

**Input Placeholder:** `[BUG_REPORT]`, `[REPRODUCTION_STEPS]`, `[FIXED_CODE_OR_DIFF]`, `[TEST_FRAMEWORK]`

**Expected Output Format:**
1. Regression test code in a fenced code block.
2. Explanation of what failure the test catches.
3. Instructions to run the test.
4. Any setup assumptions or additional cases worth covering.
