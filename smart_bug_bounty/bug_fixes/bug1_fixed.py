
def last_items(items, n):
    """Return the last n items from a list."""
    if n <= 0:
        return []
    return items[-n:]


def main():
    assert last_items([10, 20, 30, 40, 50], 3) == [30, 40, 50]
    assert last_items([10, 20, 30], 0) == []
    assert last_items([10, 20, 30], 5) == [10, 20, 30]
    assert last_items([], 2) == []
    print("bug1_fixed.py: All 4 tests passed")


if __name__ == "__main__":
    main()
