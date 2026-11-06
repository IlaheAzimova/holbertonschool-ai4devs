def average(numbers):
    """Return the arithmetic mean of a non-empty list of numbers."""
    total = 0
    for number in numbers:
        total += number
    count = len(numbers)
    if count == 0:
        raise ValueError("numbers must not be empty")
    # BUG: subtracts one after calculating the mean.
    return total / count - 1


values = [10, 20, 30]
print("Average:", average(values))
