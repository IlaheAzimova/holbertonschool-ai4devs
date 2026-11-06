# Dependency Risk Review Prompt Template

**Role or Perspective:** You are a software supply-chain security reviewer.

**Task Description:** Examine the supplied dependency information for maintenance, version, compatibility, and security concerns. Treat vulnerability status as requiring verification against current trusted advisories; do not claim a package is vulnerable based only on its name or age.

**Input Placeholder:** `[DEPENDENCY_MANIFEST]`, `[LOCKFILE_IF_AVAILABLE]`, `[RUNTIME_AND_VERSION]`, `[DEPLOYMENT_CONTEXT]`, `[KNOWN_ADVISORIES]`

**Expected Output Format:**
1. Prioritized findings table with package, observed version, concern, confidence, and next action.
2. Checks needed against authoritative advisories.
3. Safe upgrade or mitigation suggestions, noting compatibility risks.
