# Project 4
#
# Name: Geoff Blaylock
# Instructor: Turner
# Section: 09

def create_puzzle(string):
    # input is of type string
    # takes the 100 character input string and creates a 10 x 10 2-dimensional list to return
    # return value is of type list
    string = list(string)
    puzzle = [[]] * 10

    for row in range(0, 10):
        puz_row = []
        for col in range(0, 10):
            puz_row.append(string[(row * 10) + col])

        puzzle[row] = puz_row

    return puzzle


def find_word(puzzle, word):
    # input is of type list, string
    # takes a word as a string input and sends it to th three check functions to try to find it, if the word cannot
    # be found it returns a 'word not found' message
    # return value is of type string
    if check_all_cols(puzzle, word) != -1:
        return check_all_cols(puzzle, word)
    elif check_all_rows(puzzle, word) != -1:
        return check_all_rows(puzzle, word)
    elif check_all_diagonals(puzzle, word) != -1:
        return check_all_diagonals(puzzle, word)
    else:
        return word + ': word not found'


def get_words(string2):
    # input is of type string
    # splits the string of words to be searched for into a list of strings
    # return value is of type list
    str_words = string2.split()

    return str_words


def get_row(puzzle, x):
    # input is of type list, int
    # compiles a specific number row from the puzzle list into a string
    # return value is of type string
    row = ''
    for i in range(0, 10):
        row += puzzle[x][i]

    return row


def get_col(puzzle, x):
    # input is of type list, int
    # compiles a specific number column from the puzzle list into a string
    # return value is of type string
    col = ''
    for i in range(0, 10):
        col += puzzle[i][x]

    return col


def get_diagonal(puzzle, x):
    # input is of type list, int
    # compiles a specific number diagonal from the puzzle list into a string
    # return value is of type string
    diagonal = ''
    if x <= 9:
        row = 9 - x
        col = 0
        for i in range(0, 10 - row):
            diagonal += puzzle[row + i][col + i]
    elif 10 <= x <= 18:
        row = 0
        col = x - 9
        for i in range(0, 10 - col):
            diagonal += puzzle[row + i][col + i]

    return diagonal


def check_all_cols(puzzle, word):
    # input is of type list, string
    # loops through all 10 columns passing the desired word through to the check_col function for each. If the word is
    # not found in any column, -1 is returned
    # return value is of type string or int
    for i in range(0, 10):
        if check_col(puzzle, i, word) != -1:
            return check_col(puzzle, i, word)
    else:
        return -1


def check_col(puzzle, x, word):
    # input is of type list, int, string
    # looks for the desired word in the specific number column in the up and down directions, returning a string
    # displaying the word, its orientation, its row, and its column if it is found. If the word is not found, -1
    # is returned
    # return value is of type string or int
    col = get_col(puzzle, x)
    rev_col = col[::-1]
    # NOTE: I learned this method of reversing a string from a stackoverflow forum
    # https://stackoverflow.com/questions/931092/reverse-a-string-in-python
    if col.find(word) != -1:
        row = col.find(word)
        return word + ': (DOWN) row: ' + str(row) + ' column: ' + str(x)
    elif rev_col.find(word) != -1:
        row = 9 - (rev_col.find(word))
        return word + ': (UP) row: ' + str(row) + ' column: ' + str(x)
    else:
        return -1


def check_all_rows(puzzle, word):
    # input is of type list, string
    # loops through all 10 rows passing the desired word through to the check_row function for each. If the word is
    # not found in any row, -1 is returned
    # return value is of type string or int
    for i in range(0, 10):
        if check_row(puzzle, i, word) != -1:
            return check_row(puzzle, i, word)
    else:
        return -1


def check_row(puzzle, x, word):
    # input is of type list, int, string
    # looks for the desired word in the specific number row in the forward and backward directions, returning a string
    # displaying the word, its orientation, its row, and its column if it is found. If the word is not found, -1
    # is returned
    # return value is of type string or int
    row = get_row(puzzle, x)
    rev_row = row[::-1]
    # NOTE: I learned this method of reversing a string from a stackoverflow forum
    # https://stackoverflow.com/questions/931092/reverse-a-string-in-python
    if row.find(word) != -1:
        col = row.find(word)
        return word + ': (FORWARD) row: ' + str(x) + ' column: ' + str(col)
    elif rev_row.find(word) != -1:
        col = 9 - (rev_row.find(word))
        return word + ': (BACKWARD) row: ' + str(x) + ' column: ' + str(col)
    else:
        return -1


def check_all_diagonals(puzzle, word):
    # input is of type list, string
    # loops through all 19 diagonals passing the desired word through to the check_diagonal function for each. If the
    # word is not found in any diagonal, -1 is returned
    # return value is of type string or int
    for i in range(0, 19):
        if check_diagonal(puzzle, i, word) != -1:
            return check_diagonal(puzzle, i, word)
    else:
        return -1


def check_diagonal(puzzle, x, word):
    # input is of type list, int, string
    # looks for the desired word in the specific number diagonal, returning a string displaying the word, its
    # orientation, its row, and its column if it is found. If the word is not found, -1 is returned
    # return value is of type string or int
    diagonal = get_diagonal(puzzle, x)
    if diagonal.find(word) != -1:
        if x <= 9:
            row = 9 - x + diagonal.find(word)
            col = diagonal.find(word)
        else:
            row = diagonal.find(word)
            col = x - 9 + diagonal.find(word)
        return word + ': (DIAGONAL) row: ' + str(row) + ' column: ' + str(col)
    else:
        return -1
