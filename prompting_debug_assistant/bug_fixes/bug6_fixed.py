def unique_items(items):
    """Return unique items in their original order."""
    result = []

    for item in items:
        if item not in result:
            result.append(item)

    return result


if __name__ == "__main__":
    assert unique_items(
        ["red", "blue", "red", "green", "blue"]
    ) == ["red", "blue", "green"]

    assert unique_items([]) == []
    assert unique_items([1, 1, 2]) == [1, 2]

    print("bug6_fixed.py: all tests passed")
