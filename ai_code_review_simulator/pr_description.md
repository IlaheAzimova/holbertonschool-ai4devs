# Pull Request: Add Task Filtering Feature

## Summary

This pull request introduces a task filtering feature that allows users to filter tasks by status and due date. The feature makes it easier to find relevant tasks and improves task management efficiency.

## Changes

- Added a task filtering function to filter tasks by status.
- Added filtering by due date.
- Added support for combining multiple filter criteria.
- Added input validation for filter parameters.
- Added unit tests for valid filters, invalid inputs, and empty results.
- Updated the documentation to explain how to use the filtering feature.

## Context

Task management applications can become difficult to use when users have many tasks. Finding tasks by status or deadline helps users prioritize work and manage their time more effectively.

This feature addresses the need for a simple and efficient task filtering mechanism.

**Motivation:**
- Improve the user experience.
- Reduce the time needed to find specific tasks.
- Support more effective task prioritization.
- Improve code reliability through automated tests.

**Related Issue:** #42 (example issue reference)

## Testing

- Tested filtering tasks by status.
- Tested filtering tasks by due date.
- Tested combined filtering criteria.
- Tested invalid filter parameters.
- Tested behavior when no tasks match the filters.
- Verified that existing tests continue to pass.

## Implementation Details

- Added a reusable task filtering function.
- Kept filtering logic separate from other application logic.
- Included validation and error handling.
- Added unit tests to cover expected behavior and edge cases.

## Scope

This pull request focuses on basic task filtering. Advanced filtering, sorting, and pagination are outside the scope of this change.
