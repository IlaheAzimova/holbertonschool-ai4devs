# Reflection on AI-Assisted Debugging

## Introduction

In this project, I used AI assistance to investigate and fix six bugs involving Python, JavaScript, and C. The tasks included calculating averages, iterating through arrays, reading files, calculating tax, handling strings safely, and removing duplicate values. The main goal was not only to correct the code but also to understand the causes of the errors and validate the proposed solutions.

## AI Strengths

The AI performed well on bugs with clear requirements and predictable behavior. Bugs 1, 2, 4, and 6 were relatively straightforward because their solutions involved familiar programming concepts. For example, calculating an average required dividing the sum by the number of elements, while removing duplicates required preserving previously encountered values. The AI could suggest concise implementations and relevant test cases quickly.

AI assistance also helped structure the debugging process. Instead of focusing only on changing code, I could examine expected behavior, test inputs, and possible edge cases. This made it easier to organize the fixes and prepare documentation for each bug. Overall, AI reduced the time needed to identify possible solutions and provided a useful starting point for testing.

## AI Weaknesses

The more challenging bugs required closer inspection. Bug 3 involved file handling and the special case of an empty file. Bug 5 was particularly important because incorrect string handling in C can cause a buffer overflow. A solution must account for the destination buffer size, the terminating null character, and the correct header files.

The project also showed that correct-looking documentation does not guarantee that code has been executed successfully. The validation report initially failed evaluation because it did not consistently compare expected and actual outputs. This demonstrated that AI-generated explanations may be incomplete or may not satisfy a strict assessment format. Claims about test results must be supported by real execution rather than assumptions.

## Human Role

Human judgment was necessary to review the AI's suggestions, identify missing details, and ensure that the fixes matched the requirements. In particular, Bug 5 required checking the C source carefully, including the `stdio.h` header and the use of `snprintf()`. I also needed to examine the grader's feedback and improve the validation report so that every bug had clear evidence.

The human role was therefore not limited to copying code. It involved questioning suggestions, checking edge cases, interpreting feedback, and deciding whether the result was reliable.

## Conclusion

AI-assisted debugging made the process faster by generating possible fixes and test ideas. However, it was not a replacement for programming knowledge or verification. The most useful workflow was to ask AI for suggestions, inspect the code manually, run tests, and document the actual results. In real-world development, AI is best treated as a collaborative assistant: it can accelerate problem-solving, but developers remain responsible for correctness, security, and maintainability.
