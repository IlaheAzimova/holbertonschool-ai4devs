# Fix Validation Report

## bug1.py — Incorrect List Slicing

- **Original Issue:** The slice excluded the last list element and handled `n = 0` incorrectly.
- **Fix Applied:** Added a check for `n <= 0` and changed the slice to `items[-n:]`.
- **Tests:**
  1. Return the last 3 items from a list.
  2. Return an empty list when `n = 0`.
  3. Return the entire list when `n` exceeds its length.
  4. Handle an empty input list.
- **Expected Result:** All 4 tests pass.

## bug2.js — Loop Boundary Error

- **Original Issue:** The loop processed one extra element, causing the total to become `NaN`.
- **Fix Applied:** Changed the loop condition from `i <= scores.length` to `i < scores.length`.
- **Tests:**
  1. Average of `[10, 20, 30]` equals `20`.
  2. Average of `[5, 15]` equals `10`.
  3. Average of an empty array equals `0`.
- **Expected Result:** All 3 test assertions pass.

## bug3.java — Incorrect Discount Calculation

- **Original Issue:** The code subtracted the discount fraction instead of the actual discount amount.
- **Fix Applied:** Calculate the discount using `price * discountPercent / 100`.
- **Tests:**
  1. A 20% discount on 100 produces 80.
  2. A 10% discount on 50 produces 45.
  3. A 0% discount on 100 produces 100.
  4. A 100% discount on 100 produces 0.
- **Expected Result:** All 4 assertions pass with Java assertions enabled.

## bug4.py — Negative Money Transfer

- **Original Issue:** Negative and zero transfer amounts were accepted.
- **Fix Applied:** Reject transfer amounts less than or equal to zero before changing balances.
- **Tests:**
  1. A valid transfer of 20 succeeds.
  2. A negative transfer is rejected.
  3. A zero-value transfer is rejected.
  4. Invalid transfers leave both balances unchanged.
- **Expected Result:** All 4 assertions pass.

## Summary

- **Files Fixed:** 4
- **Languages Covered:** Python, JavaScript, Java
- **Validation Status:** Test cases are defined; execute the test commands to confirm the results in the local environment.
