# Project 4
#
# Name: Geoff Blaylock
# Instructor: Turner
# Section: 09

from funcs import *
import unittest


class TestCases(unittest.TestCase):

    def test_create_puzzle(self):
        string = 'WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        self.assertEqual(create_puzzle(string), puzzle)

    def test_find_word(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        word = 'GCC'
        self.assertEqual(find_word(puzzle, word), 'GCC: (DIAGONAL) row: 6 column: 5')

    def test_get_words(self):
        string = 'UNIX CALPOLY GCC SLO CPE COMPILE VIM TEST'
        words = ['UNIX', 'CALPOLY', 'GCC', 'SLO', 'CPE', 'COMPILE', 'VIM', 'TEST']
        self.assertEqual(get_words(string), words)

    def test_get_row_1(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        self.assertEqual(get_row(puzzle, 2), 'APXWKWIIIL')

    def test_get_row_2(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        self.assertEqual(get_row(puzzle, 9), 'UUIUNIXFNU')

    def test_get_col_1(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        self.assertEqual(get_col(puzzle, 5), 'TQWXMYGASI')

    def test_get_col_2(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        self.assertEqual(get_col(puzzle, 0), 'WCALPOLYXU')

    def test_get_diagonal_1(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        self.assertEqual(get_diagonal(puzzle, 4), 'OGSMN')

    def test_get_diagonal_2(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        self.assertEqual(get_diagonal(puzzle, 15), 'TEIV')

    def test_check_all_cols_1(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        word = 'CALPOLY'
        answer = 'CALPOLY: (DOWN) row: 1 column: 0'
        self.assertEqual(check_all_cols(puzzle, word), answer)

    def test_check_all_cols_2(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        word = 'GCC'
        answer = -1
        self.assertEqual(check_all_cols(puzzle, word), answer)

    def test_check_col_1(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        x = 0
        word = 'CALPOLY'
        self.assertEqual(check_col(puzzle, x, word), 'CALPOLY: (DOWN) row: 1 column: 0')

    def test_check_col_2(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        x = 8
        word = 'COMPILE'
        self.assertEqual(check_col(puzzle, x, word), 'COMPILE: (UP) row: 6 column: 8')

    def test_check_col_3(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        x = 5
        word = 'CALPOLY'
        self.assertEqual(check_col(puzzle, x, word), -1)

    def test_check_all_rows_1(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        word = 'VIM'
        answer = 'VIM: (BACKWARD) row: 1 column: 4'
        self.assertEqual(check_all_rows(puzzle, word), answer)

    def test_check_all_rows_2(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        word = 'SLO'
        answer = 'SLO: (FORWARD) row: 7 column: 2'
        self.assertEqual(check_all_rows(puzzle, word), answer)

    def test_check_all_rows_3(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        word = 'CALPOLY'
        answer = -1
        self.assertEqual(check_all_rows(puzzle, word), answer)

    def test_check_row_1(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        x = 1
        word = 'VIM'
        self.assertEqual(check_row(puzzle, x, word), 'VIM: (BACKWARD) row: 1 column: 4')

    def test_check_row_2(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        x = 2
        word = 'VIM'
        self.assertEqual(check_row(puzzle, x, word), -1)

    def test_check_all_diagonals_1(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        word = 'CPE'
        answer = 'CPE: (DIAGONAL) row: 1 column: 0'
        self.assertEqual(check_all_diagonals(puzzle, word), answer)

    def test_check_all_diagonals_2(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        word = 'UNIX'
        answer = -1
        self.assertEqual(check_all_diagonals(puzzle, word), answer)

    def test_check_diagonal_1(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        x = 8
        word = 'GCC'
        self.assertEqual(check_diagonal(puzzle, x, word), 'GCC: (DIAGONAL) row: 6 column: 5')

    def test_check_diagonal_2(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'H', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'E', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'Y'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        x = 16
        word = 'HEY'
        self.assertEqual(check_diagonal(puzzle, x, word), 'HEY: (DIAGONAL) row: 0 column: 7')

    def test_check_diagonal_3(self):
        puzzle = [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'],
                  ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'],
                  ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'],
                  ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'],
                  ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'],
                  ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'],
                  ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'],
                  ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'],
                  ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'],
                  ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]
        x = 10
        word = 'CPE'
        self.assertEqual(check_diagonal(puzzle, x, word), -1)


if __name__ == '__main__':
    unittest.main()
