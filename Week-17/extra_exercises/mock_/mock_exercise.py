def read_file_lines(filepath):
    with open(filepath, "r") as file:
        return file.read().splitlines()