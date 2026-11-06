# Structured Bug Reports

## Bug Report – `bug1_fixed.py`

- **Bug Summary:** The average calculation must handle numeric lists and empty input safely.
- **Root Cause:** Dividing by the length of an empty list causes a division-by-zero error.
- **Resolution (AI suggestion + manual edits):**
  - **AI-generated suggestion:** Calculate the average using `sum(numbers) / len(numbers)` and raise `ValueError` if the list is empty.
  - **Manual edits:** Added assertions for normal lists and empty input, plus a success message.
- **Lessons Learned:** Always test boundary cases, especially empty collections, and define clear behavior for invalid input.

## Bug Report – `bug2_fixed.js`

- **Bug Summary:** The fruit-printing loop must process every array element without accessing an invalid index.
- **Root Cause:** An incorrect loop boundary can skip the final element or access an index outside the array.
- **Resolution (AI suggestion + manual edits):**
  - **AI-generated suggestion:** Use `i < items.length` and convert each fruit name to uppercase with `toUpperCase()`.
  - **Manual edits:** Added a sample array and a completion message to verify execution.
- **Lessons Learned:** Check loop boundaries carefully and test that the final array element is processed.

## Bug Report – `bug3_fixed.py`

- **Bug Summary:** The function must return the first line of a file and handle empty files explicitly.
- **Root Cause:** An empty file returns an empty string when the first line is read, which must be handled rather than treated as valid content.
- **Resolution (AI suggestion + manual edits):**
  - **AI-generated suggestion:** Read the file using UTF-8 encoding, remove newline characters, and raise `ValueError` for an empty file.
  - **Manual edits:** Added tests for a multi-line file and an empty file, and ensured the temporary test file is removed.
- **Lessons Learned:** Test file operations with both valid content and empty files, and clean up temporary resources.

## Bug Report – `bug4_fixed.js`

- **Bug Summary:** The function must correctly calculate the total price including tax.
- **Root Cause:** The tax amount must be calculated from the price and tax rate, then added to the original price.
- **Resolution (AI suggestion + manual edits):**
  - **AI-generated suggestion:** Calculate tax with `price * taxRate` and return `price + tax`.
  - **Manual edits:** Added assertions for two price and tax-rate combinations.
- **Lessons Learned:** Verify calculations using multiple test cases and compare results against expected values.

## Bug Report – `bug5_fixed.c`

- **Bug Summary:** Copying a long string into a fixed-size character array can cause a buffer overflow.
- **Root Cause:** Copying more characters than the destination buffer can hold may overwrite memory.
- **Resolution (AI suggestion + manual edits):**
  - **AI-generated suggestion:** Use `snprintf()` with a size limit that leaves room for the null terminator.
  - **Manual edits:** Ensure the file includes `#include <stdio.h>` and add output that verifies the result.
- **Lessons Learned:** In C, always respect buffer capacity, account for the null terminator, and compile with warnings enabled.

## Bug Report – `bug6_fixed.py`

- **Bug Summary:** The function must remove duplicate items while preserving their original order.
- **Root Cause:** Returning the original list leaves duplicates in the result, while an approach that does not preserve order may change the sequence.
- **Resolution (AI suggestion + manual edits):**
  - **AI-generated suggestion:** Build a result list and append each item only if it has not already been added.
  - **Manual edits:** Added tests for duplicate strings, an empty list, and duplicate numeric values.
- **Lessons Learned:** Clarify whether output order matters and test duplicates, empty input, and different value types.
