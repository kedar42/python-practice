class Sudoku:
    def __init__(self, lines):
        self.lines = [[int(char) if char != '_' else 0 for char in line.split()] for line in lines]


def sudoku_from_file(file):
    if not validate_file(file):
        return None
    with open(file) as my_file:
        return Sudoku(my_file.readlines())


def validate_file(file):
    valid = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '_'}
    with open(file) as my_file:
        lines = my_file.readlines()
        if len(lines) != 9:
            return False
        for line in lines:
            if len(line.split()) != 9:
                return False
            for char in line.split():
                if char not in valid:
                    return False
    return True


sudoku = sudoku_from_file("input")
print("end")

