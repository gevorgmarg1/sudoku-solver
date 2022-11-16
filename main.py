import copy                                     # A library to copy the originally given board
def square_test(problem, number, i, j):         # Checks if the given number fits in the given square
    row_key = 0
    column_key = 0

    if i >= 6:
        row_key = 6
    elif i >= 3:
        row_key = 3

    if j >= 6:
        column_key = 6
    elif j >= 3:
        column_key = 3

    for m in range(row_key, row_key+3):
        for n in range(column_key, column_key+3):
            if problem[m][n] == number:
                return False
    return True
def row_test(problem, number, i, j):            # Checks if the given number fits in the given row
    if number in problem[i]:
        return False
    else:
        return True
def column_test(problem, number, i, j):         # Checks if the given number fits in the given column
    for k in problem:
        if number == k[j]:
            return False
    return True
def solve(original_problem):                    #The main function, solves the given sudoku board
    problem = copy.deepcopy(original_problem)
    number = 1
    next = True
    last_changed = [0,0]
    i = 0
    j = 0
    while i < (len(problem)):
        while j < (len(problem[i])):
            if original_problem[i][j] == 0 and next:
                if row_test(problem, number, i, j) and column_test(problem, number, i, j) and square_test(problem, number, i, j):
                    problem[i][j] = number
                    last_changed = [i, j]
                    number = 1
                    j += 1
                else:
                    if number < 9:
                        number += 1
                    else:
                        next = False
                        number = 1
            elif original_problem[i][j] != 0 and next:
                j += 1
            else:
                i = last_changed[0]
                j = last_changed[1]
                next = True
        i += 1
        j = 0
    return problem

problem = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 8 , 9, 1, 2, 3, 4, 5, 6],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
for i in solve(problem):
    print(i, "\n")
