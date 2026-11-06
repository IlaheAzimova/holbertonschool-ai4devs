# Bug Snippet Descriptions

This collection contains six intentionally flawed code samples for practicing AI-assisted debugging. Each snippet is designed to be reviewed, tested, and corrected by the learner.

## Bug 1 – `bug1.py`
**Intended Behavior:** Calculate and return the arithmetic mean of a non-empty list of numbers.  
**Issue Type:** Logical error.  
**Notes:** The returned value should be the sum divided by the number of elements. Test with `[10, 20, 30]`, whose average is `20`.

## Bug 2 – `bug2.js`
**Intended Behavior:** Print each fruit in uppercase alongside its zero-based index.  
**Issue Type:** Off-by-one error and runtime exception.  
**Notes:** The loop should visit valid array indexes only. The current loop attempts to access an element beyond the end of the array.

## Bug 3 – `bug3.py`
**Intended Behavior:** Read and return the first line of a UTF-8 text file, with the newline removed.  
**Issue Type:** Runtime exception and resource-handling issue.  
**Notes:** Consider what happens when the file does not exist or is empty. Ensure the file is closed even if reading fails.

## Bug 4 – `bug4.js`
**Intended Behavior:** Return the total price after applying a decimal tax rate. A price of `100` and a tax rate of `0.08` should produce `108`.  
**Issue Type:** Logical error / misuse of a numeric value.  
**Notes:** The tax amount should be calculated as a proportion of the price.

## Bug 5 – `bug5.c`
**Intended Behavior:** Copy a name into a fixed-size buffer and print it without writing beyond the buffer.  
**Issue Type:** Unsafe string handling / buffer overflow risk.  
**Notes:** The destination array has limited capacity, including space for the null terminator. The supplied input is too long for the buffer.

## Bug 6 – `bug6.py`
**Intended Behavior:** Return unique items in their original order. For example, `["red", "blue", "red"]` should become `["red", "blue"]`.  
**Issue Type:** Misuse of a list method and logical error.  
**Notes:** Check what `append()` returns and how the result list is updated.

## Coverage Summary
- **Logical errors:** `bug1.py`, `bug4.js`, `bug6.py`
- **Runtime exceptions / boundary conditions:** `bug2.js`, `bug3.py`
- **Off-by-one / loop logic:** `bug2.js`
- **Data type, library, or memory-safety misuse:** `bug5.c`, `bug6.py`
- **Languages:** Python, JavaScript, and C
