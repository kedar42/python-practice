def load_from_file():
    pass


def validate_file(file):
    valid = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '_'}
    with open(file) as sudoku:
        lines = sudoku.readlines()
        if len(lines) != 9:
            return False
        for line in lines:
            if len(line.split()) != 9:
                return False
            for char in line.split():
                if char not in valid:
                    return False

    return True


print(validate_file("input"))
