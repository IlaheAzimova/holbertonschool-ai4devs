def read_first_line(path):
    """Return the first line of a UTF-8 text file without its newline."""
    file = open(path, "r", encoding="utf-8")
    lines = file.readlines()
    # BUG: an empty file causes IndexError here.
    line = lines[0]
    file.close()
    return line.strip()


if __name__ == "__main__":
    filename = "sample.txt"
    print(read_first_line(filename))
