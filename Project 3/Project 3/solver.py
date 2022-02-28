# Project 1
#
# Name: Geoff Blaylock
# Instructor: Turner
# Section: 09

from solverFuncs import *


def main():
    checks = 0
    backtracks = 0
    puzzle = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    cages = get_cages()

    n = 0
    while n < 25:
        # loops through the puzzle by box number
        puzzle[get_row(n)][get_col(n)] += 1
        while not check_valid(puzzle, cages):
            # starts a loop that runs as long as the puzzle is not valid
            checks += 1
            while puzzle[get_row(n)][get_col(n)] == 5:
                # starts a loop that backtracks if the box's value is equal to 5
                puzzle[get_row(n)][get_col(n)] = 0
                n -= 1
                backtracks += 1

            puzzle[get_row(n)][get_col(n)] += 1

        checks += 1
        n += 1

    print('\n--Solution--\n')

    for r in range(0, 5):
        for c in range(0, 5):
            # loops through the entire puzzle and prints each value in a matrix format
            print(puzzle[r][c], end=' ')
        print('')

    print('\nchecks:', checks, 'backtracks:', backtracks)


if __name__ == '__main__':
    main()
