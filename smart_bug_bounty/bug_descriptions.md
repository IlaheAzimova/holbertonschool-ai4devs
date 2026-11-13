# Bug Descriptions

## bug1.py — Off-by-One Error

- **Language:** Python
- **Intended Behavior:** Return the last `n` items from a list.
- **Current Issue:** The slice `items[-n:-1]` excludes the final item. When `n` is zero, the function incorrectly returns the first item instead of an empty list.
- **Expected Fix:** Handle `n == 0` explicitly and use correct list slicing.

## bug2.js — Loop Boundary Error

- **Language:** JavaScript
- **Intended Behavior:** Calculate the average of an array of numeric scores.
- **Current Issue:** The loop condition uses `i <= scores.length`, causing an extra iteration and adding `undefined` to the total. The result becomes `NaN`.
- **Expected Fix:** Use `i < scores.length`.

## bug3.java — Incorrect Discount Calculation

- **Language:** Java
- **Intended Behavior:** Calculate the final price after applying a percentage discount.
- **Current Issue:** The function subtracts the discount fraction directly from the price instead of calculating the discount amount.
- **Expected Fix:** Calculate `price * discountPercent / 100` and subtract that amount from the original price.

## bug4.py — Missing Negative Transfer Validation

- **Language:** Python
- **Intended Behavior:** Transfer a positive amount between two existing accounts without allowing an invalid balance change.
- **Current Issue:** The function does not reject zero or negative transfer amounts. A negative amount can increase the source balance and decrease the destination balance.
- **Expected Fix:** Reject amounts less than or equal to zero before modifying either account.
