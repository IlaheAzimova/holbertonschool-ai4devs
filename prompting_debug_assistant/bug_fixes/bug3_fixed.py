def read_first_line(path):
    """Return the first line without its newline."""
    with open(path, "r", encoding="utf-8") as file:
        line = file.readline()

    if line == "":
        raise ValueError("file is empty")

    return line.rstrip("\r\n")


if __name__ == "__main__":
    import os

    test_path = "_bug3_test.txt"

    try:
        with open(test_path, "w", encoding="utf-8") as file:
            file.write("first line\nsecond line\n")

        assert read_first_line(test_path) == "first line"

        with open(test_path, "w", encoding="utf-8") as file:
            file.write("")

        try:
            read_first_line(test_path)
        except ValueError:
            pass
        else:
            raise AssertionError("Expected ValueError")

        print("bug3_fixed.py: all tests passed")
    finally:
        if os.path.exists(test_path):
            os.remove(test_path)
