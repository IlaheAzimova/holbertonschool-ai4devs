def read_first_line(path):
    """Return the first line of a UTF-8 text file, without the newline."""
    file = open(path, "r", encoding="utf-8")
    line = file.readlines()[0]
    file.close()
    return line.strip()

print(read_first_line("sample.txt"))
