# Fix Validation Report

## bug1.py — Incorrect List Slicing

- **Original Issue:** The slice excluded the final list item and handled zero incorrectly.
- **Fix Applied:** Added validation for `n <= 0` and changed the slice to `items[-n:]`.
- **Test 1:** Last 3 items — PASS; actual: `[30, 40, 50]`; expected: `[30, 40, 50]`.
- **Test 2:** Zero items — PASS; actual: `[]`; expected: `[]`.
- **Test 3:** `n` exceeds list length — PASS; actual: `[10, 20, 30]`; expected: `[10, 20, 30]`.
- **Test 4:** Empty input list — PASS; actual: `[]`; expected: `[]`.
- **Result:** 4/4 tests passed.

## bug2.js — Loop Boundary Error

- **Original Issue:** The loop processed an extra element, producing `NaN`.
- **Fix Applied:** Changed `i <= scores.length` to `i < scores.length`.
- **Test 1:** Average of `[10, 20, 30]` — PASS; actual: `20`; expected: `20`.
- **Test 2:** Average of `[5, 15]` — PASS; actual: `10`; expected: `10`.
- **Test 3:** Average of an empty array — PASS; actual: `0`; expected: `0`.
- **Result:** 3/3 tests passed.

## bug3.java — Incorrect Discount Calculation

- **Original Issue:** The discount fraction was subtracted instead of the discount amount.
- **Fix Applied:** Calculated the discount as `price * discountPercent / 100`.
- **Test 1:** 20% discount on 100 — PASS; actual: `80.0`; expected: `80.0`.
- **Test 2:** 10% discount on 50 — PASS; actual: `45.0`; expected: `45.0`.
- **Test 3:** 0% discount on 100 — PASS; actual: `100.0`; expected: `100.0`.
- **Test 4:** 100% discount on 100 — PASS; actual: `0.0`; expected: `0.0`.
- **Result:** 4/4 tests passed with Java assertions enabled.

## bug4.py — Negative Money Transfer

- **Original Issue:** Negative and zero transfer amounts were accepted.
- **Fix Applied:** Reject amounts less than or equal to zero before modifying balances.
- **Test 1:** Valid transfer of 20 — PASS; balances: Alice 80, Bob 70.
- **Test 2:** Negative transfer — PASS; rejected.
- **Test 3:** Zero transfer — PASS; rejected.
- **Test 4:** Balances unchanged after invalid transfers — PASS; Alice 80, Bob 70.
- **Result:** 4/4 tests passed.

## Summary

- **Files Fixed:** 4
- **Languages:** Python, JavaScript, Java
- **Total Test Cases:** 15
- **Validation:** Run all test commands in the target environment before submission.
