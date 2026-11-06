# Fix Validation

## Bug 1 – `bug1_fixed.py`

- **Test Input:** `[10, 20, 30]`
- **Expected Output:** `20`
- **Additional Test:** `[2, 4]` should return `3`.
- **Empty Input Test:** An empty list should raise `ValueError`.
- **Result:** Tests are included in the Python file. Run the file to confirm the results.

## Bug 2 – `bug2_fixed.js`

- **Test Input:** `["apple", "banana", "orange"]`
- **Expected Output:**
  - `0 APPLE`
  - `1 BANANA`
  - `2 ORANGE`
- **Issue Fixed:** The loop condition uses `< items.length` instead of `<= items.length`.
- **Result:** Run with Node.js and confirm that no runtime error occurs.

## Bug 3 – `bug3_fixed.py`

- **Test Input:** A file containing `first line` and `second line`.
- **Expected Output:** `first line`
- **Additional Test:** An empty file should raise `ValueError`.
- **Issue Fixed:** The code uses a context manager and handles empty files.
- **Result:** Tests are included in the Python file. Run the file to confirm the results.

## Bug 4 – `bug4_fixed.js`

- **Test Input:** `totalWithTax(100, 0.08)`
- **Expected Output:** `108`
- **Additional Test:** `totalWithTax(50, 0.1)` should return `55`.
- **Issue Fixed:** Tax is calculated by multiplying the price by the tax rate.
- **Result:** Run with Node.js and confirm that both assertions pass.

## Bug 5 – `bug5_fixed.c`

- **Test Input:** `"Alexander"` copied into an 8-byte buffer.
- **Expected Output:** The safely truncated string `Alexand`.
- **Issue Fixed:** `snprintf` limits the number of characters copied and prevents writing beyond the destination buffer.
- **Result:** Compile with a C compiler and run to confirm the output.

## Bug 6 – `bug6_fixed.py`

- **Test Input:** `["red", "blue", "red", "green", "blue"]`
- **Expected Output:** `["red", "blue", "green"]`
- **Additional Tests:** An empty list returns `[]`; `[1, 1, 2]` returns `[1, 2]`.
- **Issue Fixed:** The code calls `append()` without assigning its return value.
- **Result:** Tests are included in the Python file. Run the file to confirm the results.

## Manual Tweaks

- Added explicit validation for an empty list in the average function.
- Used a context manager to ensure the file closes after reading.
- Added an empty-file check to the first-line reader.
- Used bounded string formatting in C to prevent a buffer overflow.
- Added assertions to check expected results.
- Kept the original buggy snippets unchanged.

