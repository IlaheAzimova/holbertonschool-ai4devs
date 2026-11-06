def average(numbers):
    """Return the arithmetic mean of a non-empty list."""
    if not numbers:
        raise ValueError("numbers must not be empty")
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    assert average([10, 20, 30]) == 20
    assert average([2, 4]) == 3

    try:
        average([])
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")

    print("bug1_fixed.py: all tests passed")
