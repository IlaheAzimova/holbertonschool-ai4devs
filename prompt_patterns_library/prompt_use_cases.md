Prompt Use Cases
This document categorizes common situations where prompt patterns can improve coding workflows. Each use case defines its goal, input, and expected output.
Code Quality
- Refactoring
  - Goal: Improve readability, maintainability, and performance without changing behavior.
  - Input: Source function or module in [LANGUAGE], plus any constraints.
  - Output: Refactored code, a summary of changes, and notes about behavior preserved.
- Style Enforcement
  - Goal: Apply consistent naming, formatting, and idiomatic conventions.
  - Input: Code block and the project's style guide or conventions.
  - Output: Revised code that follows the specified style, with notable changes explained.
- Code Simplification
  - Goal: Reduce unnecessary complexity while keeping the implementation clear.
  - Input: Existing code and a description of what it should do.
  - Output: A simpler implementation and a short explanation of the trade-offs.
Debugging
- Bug Diagnosis
  - Goal: Identify the likely cause of an observed defect.
  - Input: Relevant code, error message, expected behavior, and actual behavior.
  - Output: Likely root cause, supporting reasoning, and a proposed fix.
- Error Message Explanation
  - Goal: Translate a compiler, runtime, or stack-trace error into actionable steps.
  - Input: Full error message, stack trace, environment, and relevant code.
  - Output: Plain-language explanation, likely causes, and prioritized troubleshooting steps.
- Regression Investigation
  - Goal: Find what changed and may have introduced a bug.
  - Input: Failing behavior, recent code changes, and any known-good version.
  - Output: Candidate changes, a minimal reproduction strategy, and a suggested correction.
Documentation
- Function Documentation
  - Goal: Explain a function's purpose, parameters, return values, and exceptions.
  - Input: Function implementation and documentation format, such as docstrings or JSDoc.
  - Output: Documentation consistent with the code and the requested format.
- README Generation
  - Goal: Help new contributors understand and run a project.
  - Input: Project structure, setup commands, dependencies, and main features.
  - Output: A README draft with overview, installation, usage, configuration, and examples.
- API Usage Examples
  - Goal: Show developers how to call an endpoint or library correctly.
  - Input: API specification, authentication requirements, and representative request/response shapes.
  - Output: Copyable examples, parameter explanations, and error-handling guidance.
Testing
- Unit Test Generation
  - Goal: Cover expected behavior and important edge cases for a function or class.
  - Input: Source code, test framework, and behavior requirements.
  - Output: Unit tests with descriptive names, setup, assertions, and edge cases.
- Test Case Design
  - Goal: Create a systematic set of cases from requirements.
  - Input: Feature description, acceptance criteria, and known constraints.
  - Output: A test matrix covering normal cases, boundary values, invalid input, and failure conditions.
- Regression Test Creation
  - Goal: Prevent a previously fixed bug from returning.
  - Input: Bug description, reproduction steps, and the corrected implementation.
  - Output: A regression test that fails before the fix and passes after it.
Security
- Input Validation Review
  - Goal: Find unsafe handling of untrusted input.
  - Input: Relevant code paths, input sources, and expected validation rules.
  - Output: Potential vulnerabilities, recommended validation, and safer code examples.
- Dependency Risk Review
  - Goal: Identify dependency-management concerns in a project.
  - Input: Dependency manifest and lockfile, plus the runtime environment.
  - Output: A prioritized review of outdated or risky dependencies and suggested verification steps.
Performance
- Performance Bottleneck Analysis
  - Goal: Identify likely hotspots before making optimizations.
  - Input: Relevant code, workload description, and available profiling results.
  - Output: Likely bottlenecks, measurement recommendations, and prioritized optimization ideas.
- Algorithm Complexity Review
  - Goal: Understand time and space complexity and evaluate alternatives.
  - Input: Algorithm implementation, input-size expectations, and performance constraints.
  - Output: Complexity analysis, edge cases, and possible alternative approaches.
Prompting Best Practices
For more reliable results, prompts should state the task, provide relevant context, specify constraints, define the expected output format, and ask the model to identify assumptions rather than invent missing requirements. Generated code should be reviewed and tested before being merged.
