# Unit Test Generation Prompt Template

**Role or Perspective:** You are a test engineer focused on reliable, maintainable automated tests.

**Task Description:** Generate unit tests for the supplied implementation and requirements. Cover normal behavior, boundary conditions, invalid inputs, and relevant failure cases. Use the specified framework and avoid asserting behavior that was not defined.

**Input Placeholder:** `[LANGUAGE]`, `[SOURCE_CODE]`, `[TEST_FRAMEWORK]`, `[BEHAVIOR_REQUIREMENTS]`

**Expected Output Format:**
1. Complete test code in a fenced code block.
2. Descriptive test names.
3. A brief mapping of tests to behaviors and edge cases.
4. Any assumptions or gaps in the requirements.
