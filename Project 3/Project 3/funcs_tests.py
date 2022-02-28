from solverFuncs import *
import unittest


class TestCases(unittest.TestCase):
    def test_check_valid1(self):
        puzzle = [[1, 2, 3, 0, 0], [4, 3, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        cages = [[8, 3, 1, 2, 6], [5, 2, 0, 5]]
        self.assertEqual(check_valid(puzzle, cages), True)

    def test_check_valid2(self):
        puzzle = [[1, 2, 3, 0, 0], [4, 3, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 2, 2], [0, 0, 0, 0, 0]]
        cages = [[8, 3, 1, 2, 6], [5, 2, 0, 5]]
        self.assertEqual(check_valid(puzzle, cages), False)

    def test_check_valid3(self):
        puzzle = [[1, 2, 3, 0, 5], [4, 3, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 5]]
        cages = [[8, 3, 1, 2, 6], [5, 2, 0, 5]]
        self.assertEqual(check_valid(puzzle, cages), False)

    def test_check_valid4(self):
        puzzle = [[1, 2, 3, 0, 0], [4, 3, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        cages = [[9, 3, 1, 2, 6], [5, 2, 0, 5]]
        self.assertEqual(check_valid(puzzle, cages), False)

    def test_check_all_rows1(self):
        puzzle = [[1, 5, 3, 0, 0], [2, 4, 0, 0, 0], [3, 0, 0, 0, 0], [4, 2, 0, 0, 0], [5, 1, 0, 0, 0]]
        self.assertEqual(check_all_rows(puzzle), True)

    def test_check_all_rows2(self):
        puzzle = [[1, 5, 3, 0, 0], [2, 2, 0, 0, 0], [3, 0, 0, 0, 0], [4, 2, 0, 0, 0], [5, 1, 0, 0, 0]]
        self.assertEqual(check_all_rows(puzzle), False)

    def test_check_row1(self):
        row = [1, 2, 3, 4, 5]
        self.assertEqual(check_row(row), True)

    def test_check_row2(self):
        row = [1, 1, 3, 4, 5]
        self.assertEqual(check_row(row), False)

    def test_check_all_cols1(self):
        puzzle = [[1, 5, 3, 0, 0], [2, 4, 0, 0, 0], [3, 3, 0, 0, 0], [4, 2, 0, 0, 0], [5, 1, 0, 0, 0]]
        self.assertEqual(check_all_cols(puzzle), True)

    def test_check_all_cols2(self):
        puzzle = [[2, 2, 3, 0, 0], [6, 3, 0, 0, 0], [2, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(check_all_cols(puzzle), False)

    def test_check_col1(self):
        col = [1, 2, 3, 4, 5]
        self.assertEqual(check_col(col), True)

    def test_check_col2(self):
        col = [2, 2, 3, 4, 5]
        self.assertEqual(check_col(col), False)

    def test_check_all_cages1(self):
        puzzle = [[2, 2, 3, 0, 0], [6, 3, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        cages = [[8, 3, 1, 2, 6], [5, 2, 0, 5]]
        self.assertEqual(check_all_cages(puzzle, cages), False)

    def test_check_all_cages2(self):
        puzzle = [[1, 2, 3, 0, 0], [4, 3, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        cages = [[8, 3, 1, 2, 6], [5, 2, 0, 5]]
        self.assertEqual(check_all_cages(puzzle, cages), True)

    def test_check_cage1(self):
        puzzle = [[0, 2, 3, 0, 0], [0, 3, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        cage = [8, 3, 1, 2, 6]
        self.assertEqual(check_cage(puzzle, cage), True)

    def test_check_cage2(self):
        puzzle = [[2, 0, 0, 0, 0], [6, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        cage = [5, 2, 0, 5]
        self.assertEqual(check_cage(puzzle, cage), False)

    def test_get_square_number(self):
        self.assertEqual(get_square_number(2, 4), 14)

    def test_get_row(self):
        self.assertEqual(get_row(21), 4)

    def test_get_col(self):
        self.assertEqual(get_col(17), 2)


if __name__ == '__main__':
    unittest.main()
