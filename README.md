# `py_sudoku_solver`

A brute-force sudoku solver, using iteration and backtracking.

By using iteration, we can avoid any need for tail-call optimisation in a recursive solution.

Written for and tested on Python 3.7.5

## Useage
The main function in the script is `solve()` which takes an iterable of the sudoku elements as an input, and returns a completed list.

    py_soduku_solver.solve(grid: iter) -> solved_grid: list

The input should be of len 81 to represent a sudoku board, in the order [[r0,c0], [r0,c1] ...[r8,c8]].

Empty items in the input must be `None` or empty strings / lists.
Any element outside of the 1-9 range will also be replaced with `None` by the function.