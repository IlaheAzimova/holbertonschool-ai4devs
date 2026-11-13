Objective

This document defines three benchmark coding tasks to compare development productivity with and without an AI coding assistant.

All tasks should be completed under both conditions using the same requirements and test cases.

Programming Language: Python 3

Task 1 — Email Validation

Estimated Time: 15–20 minutes

Requirements

Implement a function called is_valid_email(email) that checks whether an email address has a valid basic format.

The function should reject empty strings, addresses without an @ symbol, addresses without a domain, and addresses containing spaces.

Inputs

A string representing an email address.

Examples:

"user@example.com"

"invalid-email"

"user@"

""

Outputs

True if the email has a valid basic format.

False otherwise.

Acceptance Criteria

Returns True for "user@example.com".

Returns False for "invalid-email".

Returns False for "user@".

Returns False for an empty string.

Returns False for an email containing spaces.

Includes automated unit tests for valid and invalid inputs.

Task 2 — Word Frequency Counter

Estimated Time: 20–25 minutes

Requirements

Implement a function called count_words(text) that counts the frequency of each word in a string.

The function must:

Treat uppercase and lowercase letters as equivalent.

Ignore basic punctuation.

Return an empty dictionary when the input is empty or contains only punctuation or whitespace.

Inputs

A string containing one or more words.

Example:

"Hello, world! Hello Python."

Outputs

A dictionary containing each normalized word and its frequency.

Example:

{"hello": 2, "world": 1, "python": 1}

Acceptance Criteria

Counts repeated words correctly.

Converts words to lowercase.

Ignores basic punctuation such as commas, periods, and exclamation marks.

Returns an empty dictionary for empty input.

Handles multiple spaces and newlines.

Includes automated unit tests covering these cases.

Task 3 — Shopping Cart Total

Estimated Time: 25–30 minutes

Requirements

Implement a function called calculate_total(items) that calculates the total price of items in a shopping cart.

Each item is represented by a dictionary containing:

name: a string.

price: a non-negative number.

quantity: a non-negative integer.

The function should multiply each item's price by its quantity and return the sum.

Invalid item data should raise a ValueError. An empty shopping cart should return 0.

Inputs

A list of item dictionaries.

Example:

[
    {"name": "Book", "price": 10.0, "quantity": 2},
    {"name": "Pen", "price": 2.5, "quantity": 3}
]

Outputs

The total price as a number.

Example:

27.5

Acceptance Criteria

Calculates the total correctly for multiple items.

Returns 0 for an empty list.

Handles an item with quantity 0.

Rejects negative prices.

Rejects negative quantities.

Rejects missing required fields and invalid data types.

Rejects Boolean values for price or quantity, even though Python treats Boolean values as integers.

Includes automated unit tests for normal and invalid inputs.

Productivity Measurement Protocol

For each task, record the following metrics in both conditions:

Time taken to complete the task, in minutes.

Lines of code written.

Number of tests passed.

Number of bugs discovered during testing.

Whether all acceptance criteria were satisfied.

Conditions

Condition A: Complete the task without AI coding assistance.

Condition B: Complete the same task with GitHub Copilot or another AI coding assistant.

Use the same requirements and test cases in both conditions. Record actual results without estimating or inventing measurements.

Comparison Goal

Compare completion time, correctness, code quality, and testing results to evaluate the practical impact of AI coding assistance.
