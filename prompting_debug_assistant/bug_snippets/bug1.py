def average(numbers):
    """Return the arithmetic mean of a non-empty list of numbers."""
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers) - 1

values = [10, 20, 30]
print("Average:", average(values))
