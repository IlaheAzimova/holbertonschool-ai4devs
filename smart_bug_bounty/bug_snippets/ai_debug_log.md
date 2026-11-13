# AI Debug Log

## bug1.py — Incorrect List Slicing

**AI Explanation:** The function `last_items()` uses `items[-n:-1]`, which excludes the last element of the list. When `n == 0`, it returns the first element instead of an empty list.

**Suggested Fix:**
```python
def last_items(items, n):
    if n <= 0:
        return []
    return items[-n:]
```

**Confidence:** High

## bug2.js — Loop Boundary Error

**AI Explanation:** The loop condition `i <= scores.length` allows one extra iteration. During that iteration, `scores[i]` is `undefined`, so adding it to `total` produces `NaN`. The average calculation therefore fails.

**Suggested Fix:**
```javascript
for (let i = 0; i < scores.length; i++) {
    total += scores[i];
}
```

**Confidence:** High

## bug3.java — Incorrect Discount Calculation

**AI Explanation:** The code calculates the discount fraction using `discountPercent / 100` but subtracts that fraction directly from the original price. For example, a 20% discount on 100 should produce 80, but the current code returns 99.8.

**Suggested Fix:**
```java
double discount = price * discountPercent / 100;
return price - discount;
```

**Confidence:** High

## bug4.py — Negative Money Transfer

**AI Explanation:** The function `transfer_balance()` does not validate that the transfer amount is positive. A negative amount can increase the source account balance and decrease the destination account balance.

**Suggested Fix:**
```python
if amount <= 0:
    return False
```

Place this validation before modifying either account balance.

**Confidence:** High
