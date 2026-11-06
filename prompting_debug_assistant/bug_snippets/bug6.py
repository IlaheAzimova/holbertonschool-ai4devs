def unique_items(items):
    """Return the items in first-seen order, with duplicates removed."""
    result = []
    for item in items:
        if item not in result:
            result = result.append(item)
    return result

print(unique_items(["red", "blue", "red"]))
