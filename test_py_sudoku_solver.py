import unittest
import types

from py_sudoku_solver import solve, all_conditions_met, conditions_met, calc_subgroup_indices, duplicates, row, col, square, square_indexes, printable_grid

    
    ##### ---------------- Test grids ---------------- #####    

grid_one = [
    2,None, 9, None, 8, None, 5, None, None,
    None, None, 4, 7, 6, 9, None, None, None,
    3,None, None, None, 1, 2, None, 4, None,
    None, None, 3, 6, None, None, None, 5, 4,
    None, 4, None, None, None, None, None, 8, None,
    8,5, None, None, None, 7, 6, None, None,
    None, 2, None, 8, 7, None, None, None, 9,
    None, None, None, 1, 9, 6, 2, None, None,
    None, None, 5, None, 4, None, 1, None, 8
]

grid_one_solved = [
    2, 6, 9, 3, 8, 4, 5, 1, 7,
    5, 1, 4, 7, 6, 9, 8, 2, 3,
    3, 8, 7, 5, 1, 2, 9, 4, 6,
    1, 9, 3, 6, 2, 8, 7, 5, 4,
    7, 4, 6, 9, 5, 1, 3, 8, 2,
    8, 5, 2, 4, 3, 7, 6, 9, 1,
    6, 2, 1, 8, 7, 5, 4, 3, 9,
    4, 3, 8, 1, 9, 6, 2, 7, 5,
    9, 7, 5, 2, 4, 3, 1, 6, 8
]

grid_two = [
    None, None, None, 6, 7, None, None, 4, None,
    1, None, None, None, None, None, None, 3, 6,
    None, 4, 2, 1, None, None, None, None, None,
    4, None, None, 7, None, None, None, None, None,
    None, None, 5, None, None, None, 3, None, None,
    None, None, None, None, None, 2, None, None, 8,
    None, None, None, None, None, 1, 6, 7, None,
    5, 8, None, None, None, None, None, None, 3,
    None, 3, None, None, 2, 9, None, None, None
]

grid_two_solved = [
    3, 5, 9, 6, 7, 8, 1, 4, 2,
    1, 7, 8, 2, 9, 4, 5, 3, 6,
    6, 4, 2, 1, 5, 3, 7, 8, 9,
    4, 2, 3, 7, 8, 5, 9, 6, 1,
    8, 1, 5, 9, 4, 6, 3, 2, 7,
    9, 6, 7, 3, 1, 2, 4, 5, 8,
    2, 9, 4, 8, 3, 1, 6, 7, 5,
    5, 8, 1, 4, 6, 7, 2, 9, 3,
    7, 3, 6, 5, 2, 9, 8, 1, 4
]


    ##### ---------------- Component tests ---------------- #####    

class TestDuplicates(unittest.TestCase):
    
    def test_range(self):
        res = duplicates(range(10))
        self.assertFalse(res)

    def test_w_dupe_no(self):
        arg = [1, 1, 4, 5, 6, None]
        res = duplicates(arg)
        self.assertTrue(res)

    def test_w_dupe_Nones(self):
        """
        None's should be ignored by the function
        """
        arg = [1, 2, 3, 4, 5, 6, None, None]
        res = duplicates(arg)
        self.assertFalse(res)

class TestAllConditionsMet(unittest.TestCase):

    def test_unfinished_grid(self):
        res = all_conditions_met(list(grid_one))
        self.assertTrue(res)

    def test_finished_grid(self):
        res = all_conditions_met(list(grid_one_solved))
        self.assertTrue(res)

    def test_wrong_grid(self):
        self.grid_one_wrong = list(grid_one)
        self.grid_one_wrong[10] = 2
        res = all_conditions_met(self.grid_one_wrong)
        self.assertFalse(res)

class TestConditionsMet(unittest.TestCase):
    
    def test_unfinished_grid_i1(self):
        res = conditions_met(list(grid_one), 1)
        self.assertTrue(res)

    def test_finished_grid_i1(self):
        res = conditions_met(list(grid_one_solved),1)
        self.assertTrue(res)

    def test_wrong_grid_i10(self):
        self.grid_one_wrong = list(grid_one)
        self.grid_one_wrong[10] = 2
        res = conditions_met(self.grid_one_wrong, 10)
        self.assertFalse(res)

class TestCalcSubgroupIndices(unittest.TestCase):

    def test_index_1(self):
        index = 1
        corr_row_i, corr_col_i, corr_sqr_i = (0, 1, 0)
        row_i, col_i, sqr_i = calc_subgroup_indices(index)
        self.assertEqual((row_i, col_i, sqr_i), (corr_row_i, corr_col_i, corr_sqr_i))

    def test_index_40(self):
        index = 40
        corr_row_i, corr_col_i, corr_sqr_i = (4, 4, 4)
        row_i, col_i, sqr_i = calc_subgroup_indices(index)
        self.assertEqual((row_i, col_i, sqr_i), (corr_row_i, corr_col_i, corr_sqr_i))

    def test_index_80(self):
        index = 80
        corr_row_i, corr_col_i, corr_sqr_i = (8, 8, 8)
        row_i, col_i, sqr_i = calc_subgroup_indices(index)
        self.assertEqual((row_i, col_i, sqr_i), (corr_row_i, corr_col_i, corr_sqr_i))

class TestRow(unittest.TestCase):

    def test_row(self):
        res = row(1)
        correct_res = slice(9, 18, None)
        self.assertEqual(res, correct_res)

class TestCol(unittest.TestCase):

    def test_col(self):
        res = col(1)
        correct_res = slice(1, None, 9)
        self.assertEqual(res, correct_res)

class TestSquare(unittest.TestCase):

    def test_square_is_gen(self):
        """
        square should return a generator obj
        """
        res = isinstance(square(grid_one, 1), types.GeneratorType)
        self.assertTrue(res)

    def test_square_with_grid(self):
        res = list(square(grid_one, 1))
        correct_res = [None, 8, None, 7, 6, 9, None, 1, 2]
        self.assertEqual(res, correct_res)

    def test_square_with_range(self):
        res = list(square(range(81), 1))
        correct_res = [3, 4, 5, 12, 13, 14, 21, 22, 23]
        self.assertEqual(res, correct_res)


class TestSquareIndexes(unittest.TestCase):

    def test_square_ind_is_gen(self):
        """
        square_indexes should return a generator obj
        """
        res = isinstance(square_indexes(1), types.GeneratorType)
        self.assertTrue(res)

    def test_square_ind(self):
        res = list(square_indexes(1))
        correct_res = [3, 4, 5, 12, 13, 14, 21, 22, 23]
        self.assertEqual(res, correct_res)

class TestPrintableGrid(unittest.TestCase):

    def test_printable_grid(self):
        res = printable_grid(grid_one_solved)
        self.assertEqual(res[0], [2, 6, 9, 3, 8, 4, 5, 1, 7])
        self.assertEqual(res[8], [9, 7, 5, 2, 4, 3, 1, 6, 8])
        self.assertEqual(len(res), 9)

    ##### ---------------- Main functionality tests ---------------- #####    
        
class TestSolve(unittest.TestCase):

    def test_solve_g1(self):
        res = solve(list(grid_one))
        self.assertEqual(res, list(grid_one_solved))

    def test_solve_g2(self):
        res = solve(list(grid_two))
        self.assertEqual(res, list(grid_two_solved))

    def test_solve_unsolvable(self):
        """
        Currently the solve() function just fails when an unsolvable array is added.
        This needs to be more graceful. Maybe return None?
        """
        with self.assertRaises(IndexError):
            solve(list(range(1,10))*9)

        with self.assertRaises(TypeError):
            solve(range(81))


if __name__ == '__main__':
    unittest.main()