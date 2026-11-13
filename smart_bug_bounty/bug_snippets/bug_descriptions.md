# Bug Descriptions

## bug1.py — Incorrect List Slicing
- **Language:** Python
- **Intended Behavior:** Return the last `n` items from a list.
- **Current Issue:** The slice excludes the final list item. When `n` is zero, the function incorrectly returns the first item.
- **Expected Fix:** Handle zero explicitly and correct the slicing logic.

## bug2.js — Loop Boundary Error
- **Language:** JavaScript
- **Intended Behavior:** Calculate the average of an array of numbers.
- **Current Issue:** The loop uses `i <= scores.length`, causing an extra iteration and making the result `NaN`.
- **Expected Fix:** Change the loop condition to `i < scores.length`.

## bug3.java — Incorrect Discount Calculation
- **Language:** Java
- **Intended Behavior:** Calculate the final price after a percentage discount.
- **Current Issue:** The code subtracts the discount fraction instead of the actual discount amount.
- **Expected Fix:** Calculate the discount as `price * discountPercent / 100` and subtract it from the original price.

## bug4.py — Negative Money Transfer
- **Language:** Python
- **Intended Behavior:** Transfer a positive amount between two existing accounts.
- **Current Issue:** Negative transfer amounts are accepted and can increase the source balance while decreasing the destination balance.
- **Expected Fix:** Reject amounts less than or equal to zero before changing either balance.
