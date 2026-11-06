# Bug Snippet Descriptions

This collection contains intentionally flawed examples for practicing AI-assisted debugging. Each snippet describes the intended behavior without giving away a full solution.

## Bug 1 – `bug1.py`
**Intended Behavior:** Calculate and return the arithmetic mean of a non-empty list of numbers.  
**Issue Type:** Logical error.  
**Notes:** The returned value should be the sum divided by the number of elements. Test with `[10, 20, 30]`.

## Bug 2 – `bug2.js`
**Intended Behavior:** Print each fruit in uppercase alongside its zero-based index.  
**Issue Type:** Off-by-one error and runtime exception.  
**Notes:** The loop should visit valid array indexes only. The current loop attempts to access an element beyond the end of the array.

## Bug 3 – `bug3.py`
**Intended Behavior:** Read and return the first line of a UTF-8 text file, with surrounding whitespace and the newline removed.  
**Issue Type:** Runtime exception and resource-handling issue.  
**Notes:** Consider what happens when the file does not exist or is empty, and ensure the file is closed even if reading fails.

## Bug 4 – `bug4.js`
**Intended Behavior:** Return the total price after applying a decimal tax rate. For example, a price of `100` with a tax rate of `0.08` should produce `108`.  
**Issue Type:** Logical error and misuse of a numeric value.  
**Notes:** The tax amount should be calculated as a proportion of the price.

## Bug 5 – `bug5.c`
**Intended Behavior:** Copy a name into a fixed-size buffer and print it without writing beyond the buffer.  
**Issue Type:** Unsafe string handling / buffer overflow risk.  
**Notes:** The destination array can hold only a limited number of characters including the null terminator. The supplied input is longer than the buffer can safely store.

## Bug 6 – `bug6.py`
**Intended Behavior:** Return a list of unique items in their original order. For example, `["red", "blue", "red"]` should become `["red", "blue"]`.  
**Issue Type:** Misuse of a list method and logical error.  
**Notes:** Check the return value of `append()` and how the result list is updated.

## Coverage Summary

- **Syntax errors:** The snippets focus on logical, runtime, loop, resource-handling, and unsafe data-handling bugs rather than deliberately invalid syntax, so students can practice diagnosing more than parser errors.
- **Logical errors:** `bug1.py`, `bug4.js`, `bug6.py`
- **Runtime exceptions / boundary conditions:** `bug2.js`, `bug3.py`
- **Off-by-one / loop logic:** `bug2.js`
- **Data type, library, or memory-safety misuse:** `bug5.c`, `bug6.py`
