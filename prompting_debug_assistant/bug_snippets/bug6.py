def unique_items(items):
    """Return unique items in their original order."""
    result = []
    for item in items:
        if item not in result:
            # BUG: append mutates the list and returns None.
            result = result.append(item)
    return result


colors = ["red", "blue", "red", "green", "blue"]
print(unique_items(colors))
