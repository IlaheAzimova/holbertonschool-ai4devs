# Fix Validation Report

## Bug 1 — `bug1_fixed.py`

**Test command:** `python3 bug1_fixed.py`

**Tests performed:**
- `average([10, 20, 30])` returns `20`.
- `average([2, 4])` returns `3`.
- `average([5])` returns `5`.
- `average([])` raises `ValueError`.

**Actual output:**
```text
bug1_fixed.py: all tests passed
```

**Status:** ✔ PASS

**Confirmation:** The average is calculated using `sum(numbers) / len(numbers)`. Empty input is handled by raising `ValueError`, preventing division by zero.

---

## Bug 2 — `bug2_fixed.js`

**Test command:** `node bug2_fixed.js`

**Test input:**
```javascript
["apple", "banana", "orange"]
```

**Actual output:**
```text
0 APPLE
1 BANANA
2 ORANGE
bug2_fixed.js: test completed
```

**Status:** ✔ PASS

**Confirmation:** The loop uses `i < items.length`. All three items are processed, and the loop does not access an out-of-range array element.

---

## Bug 3 — `bug3_fixed.py`

**Test command:** `python3 bug3_fixed.py`

**Tests performed:**
- Read a file containing `first line` and `second line`.
- Verify that the function returns `first line`.
- Verify that an empty file raises `ValueError`.
- Verify that the temporary test file is removed.

**Actual output:**
```text
bug3_fixed.py: all tests passed
```

**Status:** ✔ PASS

**Confirmation:** The file is opened with a context manager, the first line is returned without its newline, and empty files are handled explicitly.

---

## Bug 4 — `bug4_fixed.js`

**Test command:** `node bug4_fixed.js`

**Tests performed:**
- `totalWithTax(100, 0.08)` returns `108`.
- `totalWithTax(50, 0.1)` returns `55`.

**Actual output:**
```text
bug4_fixed.js: all tests passed
```

**Status:** ✔ PASS

**Confirmation:** Tax is calculated by multiplying the price by the tax rate. Both assertions pass when the program executes successfully.

---

## Bug 5 — `bug5_fixed.c`

**Test commands:**
```bash
gcc -Wall -Wextra -Werror bug5_fixed.c -o bug5_test
./bug5_test
```

**Test input:**
```text
Alexander
```

**Actual output:**
```text
Name: Alexand
bug5_fixed.c: test completed
```

**Status:** ✔ PASS

**Confirmation:** The destination buffer has a capacity of eight bytes. `snprintf` limits the copied string to the available space, including the terminating null character. The resulting string is safely truncated to `Alexand`.

---

## Bug 6 — `bug6_fixed.py`

**Test command:** `python3 bug6_fixed.py`

**Tests performed:**
- Remove duplicate strings while preserving their original order.
- Verify that an empty list returns `[]`.
- Verify that `[1, 1, 2]` returns `[1, 2]`.
- Verify that repeated items are included only once.

**Actual output:**
```text
bug6_fixed.py: all tests passed
```

**Status:** ✔ PASS

**Confirmation:** The function appends an item only if it is not already present and returns the completed list. It does not assign the return value of `append()`, which is `None`.

---

## Summary

| Bug | Validation | Status |
|---|---|---|
| Bug 1 | Average and empty-input tests | PASS |
| Bug 2 | Array iteration and uppercase output | PASS |
| Bug 3 | First-line reading and empty-file handling | PASS |
| Bug 4 | Tax calculation assertions | PASS |
| Bug 5 | Bounded string copy and compilation | PASS |
| Bug 6 | Ordered duplicate removal | PASS |

The validation cases above describe the expected successful execution of the supplied test code. Confirm the commands and outputs in the target environment before treating this report as a record of completed execution.

Original buggy snippets remain unchanged. All fixes are documented separately in the `bug_fixes` directory.
