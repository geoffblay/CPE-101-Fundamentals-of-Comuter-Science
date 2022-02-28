# Project 4
#
# Name: Geoff Blaylock
# Instructor: Turner
# Section: 09

from funcs import *


def main():
    inp = input('')
    inp2 = input('')
    puzzle = create_puzzle(inp)
    words = get_words(inp2)

    print('Puzzle:\n')

    for row in range(0, 10):
        for col in range(0, 10):
            # loops through the 100 character input string and prints it in 10 x 10 format
            print(puzzle[row][col], end='')
        print('')
    print('')

    for i in range(0, len(words)):
        # loops through each word in the 2nd input string passing them into the search functions
        print(find_word(puzzle, words[i]))


if __name__ == '__main__':
    main()
