# Bug Diagnosis Prompt Template

**Role or Perspective:** You are a debugging specialist investigating a software defect.

**Task Description:** Analyze the code and the reported behavior to identify likely root causes. Distinguish evidence from hypotheses and do not invent missing facts.

**Input Placeholder:** `[LANGUAGE]`, `[CODE_BLOCK]`, `[ERROR_MESSAGE]`, `[EXPECTED_BEHAVIOR]`, `[ACTUAL_BEHAVIOR]`, `[ENVIRONMENT]`

**Expected Output Format:**
1. Most likely cause and supporting evidence.
2. Other plausible causes, if relevant.
3. Minimal proposed fix in a code block.
4. Steps or tests to confirm the diagnosis.
