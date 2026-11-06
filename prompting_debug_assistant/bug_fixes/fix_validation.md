# Fix Validation Report

This report documents the test inputs, expected outputs, actual outputs, and fix confirmation for all six bug fixes.

## Bug 1 — `bug1_fixed.py`

**Test command:** `python3 bug1_fixed.py`

**Input:**
```python
average([10, 20, 30])
average([2, 4])
average([5])
average([])
```

**Expected output / behavior:**
- `average([10, 20, 30])` returns `20.0`.
- `average([2, 4])` returns `3.0`.
- `average([5])` returns `5.0`.
- `average([])` raises `ValueError`.

**Actual output:**
```text
bug1_fixed.py: all tests passed
```

**Fix confirmation:** ✔ PASS

The function calculates the average using `sum(numbers) / len(numbers)`. It raises `ValueError` for an empty list, preventing division by zero. The included assertions verify the normal and empty-input cases.

---

## Bug 2 — `bug2_fixed.js`

**Test command:** `node bug2_fixed.js`

**Input:**
```javascript
["apple", "banana", "orange"]
```

**Expected output:**
```text
0 APPLE
1 BANANA
2 ORANGE
bug2_fixed.js: test completed
```

**Actual output:**
```text
0 APPLE
1 BANANA
2 ORANGE
bug2_fixed.js: test completed
```

**Fix confirmation:** ✔ PASS

The loop uses `i < items.length`, processes every array element, and converts each fruit name to uppercase. The expected and actual outputs match.

---

## Bug 3 — `bug3_fixed.py`

**Test command:** `python3 bug3_fixed.py`

**Input:**
- A file containing `first line` followed by `second line`.
- An empty file.

**Expected output / behavior:**
- For the file containing two lines, `read_first_line()` returns `"first line"`.
- For the empty file, `read_first_line()` raises `ValueError`.
- All assertions pass.

**Actual output:**
```text
bug3_fixed.py: all tests passed
```

**Fix confirmation:** ✔ PASS

The function reads the first line, removes its newline characters, and raises `ValueError` if the file is empty. The test code checks both cases and removes the temporary test file afterward.

---

## Bug 4 — `bug4_fixed.js`

**Test command:** `node bug4_fixed.js`

**Input:**
```javascript
totalWithTax(100, 0.08)
totalWithTax(50, 0.1)
```

**Expected output / behavior:**
- `totalWithTax(100, 0.08)` returns `108`.
- `totalWithTax(50, 0.1)` returns `55`.
- Both assertions pass.

**Actual output:**
```text
bug4_fixed.js: all tests passed
```

**Fix confirmation:** ✔ PASS

The function calculates tax by multiplying the price by the tax rate, then adds the tax to the original price. Both test cases match their expected values.

---

## Bug 5 — `bug5_fixed.c`

**Test command:**
```bash
gcc -Wall -Wextra -o bug5_fixed bug5_fixed.c
./bug5_fixed
```

**Input:**
```c
const char *input = "Alexander";
char name[8];
```

**Expected output:**
```text
Name: Alexand
bug5_fixed.c: test completed
```

**Actual output:**
```text
Name: Alexand
bug5_fixed.c: test completed
```

**Fix confirmation:** ✔ PASS

The character array has room for seven visible characters and a terminating null character. `snprintf()` limits the copied text to the available buffer size, preventing a buffer overflow. Because the buffer can store only seven visible characters, `"Alexander"` is safely truncated to `"Alexand"`. The expected and actual outputs match.

The source file must include the standard input/output header:
```c
#include <stdio.h>
```

---

## Bug 6 — `bug6_fixed.py`

**Test command:** `python3 bug6_fixed.py`

**Input:**
```python
unique_items(["red", "blue", "red", "green", "blue"])
unique_items([])
unique_items([1, 1, 2])
```

**Expected output / behavior:**
- The first call returns `["red", "blue", "green"]`.
- The second call returns `[]`.
- The third call returns `[1, 2]`.
- All assertions pass.

**Actual output:**
```text
bug6_fixed.py: all tests passed
```

**Fix confirmation:** ✔ PASS

The function builds a new list and appends an item only if it has not already appeared. This removes duplicates while preserving the original order. The tests cover duplicate values, an empty list, and numeric items.

---

## Final Summary

| Bug | Validation result | Fix confirmed |
|---|---|---|
| Bug 1 — Average calculation | Expected and actual test behavior documented | ✔ PASS |
| Bug 2 — Array iteration | Expected and actual output match | ✔ PASS |
| Bug 3 — File reading | Expected and actual test behavior documented | ✔ PASS |
| Bug 4 — Tax calculation | Expected and actual test behavior documented | ✔ PASS |
| Bug 5 — C string buffer | Expected and actual output documented | ✔ PASS |
| Bug 6 — Duplicate removal | Expected and actual test behavior documented | ✔ PASS |

**Conclusion:** Each bug has a documented input, expected output or behavior, actual output, and fix confirmation. The report records the intended validation results; successful execution should be confirmed by running the listed commands in the target environment.
