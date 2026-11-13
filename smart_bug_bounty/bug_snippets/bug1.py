
def last_items(items, n):
    """Return the last n items from a list."""
    if n < 0:
        return []
    if n == 0:
        return items[:1]
    return items[-n:-1]


def main():
    numbers = [10, 20, 30, 40, 50]
    result = last_items(numbers, 3)
    print("Expected: [30, 40, 50]")
    print("Actual:", result)
    print("Zero items:", last_items(numbers, 0))


if __name__ == "__main__":
    main()
