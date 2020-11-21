# write a function that checks if a given solution to sudoku is valid
# function must check all 3 areas:
# - rows
# - columns
# - mini square-shaped sections with 3-unit length side
# conditions of correct solution to sudoku:
# - only digits from 1 to 9
# - only unique digits

# valid_solution([
#   [5, 3, 4, 6, 7, 8, 9, 1, 2],
#   [6, 7, 2, 1, 9, 5, 3, 4, 8],
#   [1, 9, 8, 3, 4, 2, 5, 6, 7],
#   [8, 5, 9, 7, 6, 1, 4, 2, 3],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 6, 1, 5, 3, 7, 2, 8, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]);
# # => true
#
# valid_solution([
#   [5, 3, 4, 6, 7, 8, 9, 1, 2],
#   [6, 7, 2, 1, 9, 0, 3, 4, 8],
#   [1, 0, 0, 3, 4, 2, 5, 6, 0],
#   [8, 5, 9, 7, 6, 1, 0, 2, 0],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 0, 1, 5, 3, 7, 2, 1, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 0, 0, 4, 8, 1, 1, 7, 9]
# ]);
# # => false


def valid_solution(sudoku_board):
    def valid_collection(sudoku_collection):
        correctness = sum(sudoku_collection) == 45
        uniqueness = len(sudoku_collection) == len(set(sudoku_collection))
        minimal_val = min(sudoku_collection) == 1
        maximum_val = max(sudoku_collection) == 9
        return all((correctness, uniqueness, minimal_val, maximum_val))

    def check_rows(sudoku_board):
        for row in sudoku_board:
            if not valid_collection(row):
                return False
        return True

    def check_columns(sudoku_board):
        for i in range(9):
            column = []
            for row in sudoku_board:
                column.append(row[i])
            if not valid_collection(row):
                return False
        return True

    def check_sections(sudoku_board):
        sections = []
        index_groups = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for indexes in index_groups:
            for indexes2 in index_groups:
                section = []
                for i in indexes2:
                    [
                        section.append(x)
                        for x in sudoku_board[i][indexes[0] : indexes[-1] + 1]
                    ]
                sections.append(section)
        for section in sections:
            if not valid_collection(section):
                return False
        return True

    def check_all(sudoku_board):
        checks = [check_rows, check_columns, check_sections]
        for f in checks:
            if not f(sudoku_board):
                return False
        return True

    return check_all(sudoku_board)


board_1 = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

board_2 = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 0, 3, 4, 8],
    [1, 0, 0, 3, 4, 2, 5, 6, 0],
    [8, 5, 9, 7, 6, 1, 0, 2, 0],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 0, 1, 5, 3, 7, 2, 1, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 0, 0, 4, 8, 1, 1, 7, 9],
]

assert valid_solution(board_1)
assert not valid_solution(board_2)
