# Project 1
#
# Name: Geoff Blaylock
# Instructor: Turner
# Section: 09

def check_valid(puzzle, cages):
    # input is of type list
    # calls every checking function to see if the entire puzzle is currently valid
    # return value is of type boolean
    if check_all_rows(puzzle) and check_all_cols(puzzle) and check_all_cages(puzzle, cages):
        return True
    else:
        return False


def check_all_rows(puzzle):
    # input is of type list
    # calls the check_row function 5 times to see if all of the rows are valid yet
    # return value is of type boolean
    row0 = puzzle[0]
    row1 = puzzle[1]
    row2 = puzzle[2]
    row3 = puzzle[3]
    row4 = puzzle[4]
    if (check_row(row0)) and (check_row(row1)) and (check_row(row2)) and (
            check_row(row3)) and (check_row(row4)):
        return True
    else:
        return False


def check_row(row):
    # input is of type list
    # checks the passed in list to see if there are any duplicate integers
    # return value is of type boolean
    if row.count(1) > 1:
        return False
    if row.count(2) > 1:
        return False
    if row.count(3) > 1:
        return False
    if row.count(4) > 1:
        return False
    if row.count(5) > 1:
        return False
    else:
        return True


def check_all_cols(puzzle):
    # input is of type list
    # calls the check_col function 5 times to see if all of the columns are valid yet
    # return value is of type boolean
    col0 = [puzzle[0][0], puzzle[1][0], puzzle[2][0], puzzle[3][0], puzzle[4][0]]
    col1 = [puzzle[0][1], puzzle[1][1], puzzle[2][1], puzzle[3][1], puzzle[4][1]]
    col2 = [puzzle[0][2], puzzle[1][2], puzzle[2][2], puzzle[3][2], puzzle[4][2]]
    col3 = [puzzle[0][3], puzzle[1][3], puzzle[2][3], puzzle[3][3], puzzle[4][3]]
    col4 = [puzzle[0][4], puzzle[1][4], puzzle[2][4], puzzle[3][4], puzzle[4][4]]
    if (check_col(col0)) and (check_col(col1)) and (check_col(col2)) and (
            check_col(col3)) and (check_col(col4)):
        return True
    else:
        return False


def check_col(col):
    # input is of type list
    # checks the passed in list to see if there are any duplicate integers
    # return value is of type boolean
    if col.count(1) > 1:
        return False
    if col.count(2) > 1:
        return False
    if col.count(3) > 1:
        return False
    if col.count(4) > 1:
        return False
    if col.count(5) > 1:
        return False
    else:
        return True


def check_all_cages(puzzle, cages):
    # input is of type list
    # calls the check_cage function once for every cage generated to see if all of the cages are valid yet
    # return value is of type boolean
    num_cages = int(len(cages))
    valid = 0

    for i in range(0, num_cages):
        if check_cage(puzzle, cages[i]):
            valid += 1
        else:
            valid += 0

    if valid == num_cages:
        return True
    else:
        return False


def check_cage(puzzle, cage):
    # input is of type list
    # checks to see if the passed in cage is full and if the values of the boxes represented in the cage add
    # up to the cage's desired sum
    # return value is of type boolean
    total = 0
    full = False

    for i in range(2, int(len(cage))):
        if puzzle[get_row(cage[i])][get_col(cage[i])] != 0:
            full = True
        else:
            full = False

    for i in range(2, int(len(cage))):
        total += puzzle[get_row(cage[i])][get_col(cage[i])]

    if not full and total < cage[0]:
        return True
    elif full and total == cage[0]:
        return True
    else:
        return False


def get_square_number(row, col):
    # input is of type int
    # returns the box number (0-24) when given the box's row and column
    # return value is of type int
    return (5 * row) + col


def get_row(number):
    # input is of type int
    # returns the box's row number when given the box number
    # return value is of type int
    return number // 5


def get_col(number):
    # input is of type int
    # returns the box's column number when given the box number
    # return value is of type int
    return number % 5


def get_cages():
    # function has no input
    # prompts the user for the number of cages and then the corresponding 'code' for each cage in the puzzle.
    # the function then compiles this data into a list of lists
    # return value is of type list
    num_cages = int(input("Number of cages:"))
    cages = [[]] * num_cages

    for i in range(0, num_cages):
        print("Cage number ", end='')
        print(i, end='')

        string = input(': ')
        string_list = string.split()
        int_list = []

        for j in range(0, len(string_list)):
            int_list.append(int(string_list[j]))

        cages[i] = int_list

    return cages
