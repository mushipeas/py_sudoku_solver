# `py_sudoku_solver`

A brute-force sudoku solver, using iteration and backtracking.

By using iteration, we can avoid any need for tail-call optimisation in a recursive solution.

Written for and tested on Python 3.7.5

## Useage

### solve()
The main function in the script is `solve()` which takes an iterable of the sudoku elements as an input, and returns a completed list.

    py_soduku_solver.solve(grid: iter) -> solved_grid: list

The input should be of len 81 to represent a sudoku board, in the order [[r0,c0], [r0,c1] ...[r8,c8]].

Empty items in the input must be `None` or empty strings / lists.
Any element outside of the 1-9 range will also be replaced with `None` by the function.

### print_grid()
The `print_grid()` function can display the list in a more viewable form:

    py_soduku_solver.print_grid(grid: iter) -> None

Which outputs:

        [3, 5, 9, 6, 7, 8, 1, 4, 2]
        [1, 7, 8, 2, 9, 4, 5, 3, 6]
        [6, 4, 2, 1, 5, 3, 7, 8, 9]
        [4, 2, 3, 7, 8, 5, 9, 6, 1]
        [8, 1, 5, 9, 4, 6, 3, 2, 7]
        [9, 6, 7, 3, 1, 2, 4, 5, 8]
        [2, 9, 4, 8, 3, 1, 6, 7, 5]
        [5, 8, 1, 4, 6, 7, 2, 9, 3]
        [7, 3, 6, 5, 2, 9, 8, 1, 4]

Items which are `None` are replaced with `0` for printing, to ensure correct spacing, i.e:

        [0, 0, 0, 6, 7, 0, 0, 4, 0]
        [1, 0, 0, 0, 0, 0, 0, 3, 6]
        [0, 4, 2, 1, 0, 0, 0, 0, 0]
        [4, 0, 0, 7, 0, 0, 0, 0, 0]
        [0, 0, 5, 0, 0, 0, 3, 0, 0]
        [0, 0, 0, 0, 0, 2, 0, 0, 8]
        [0, 0, 0, 0, 0, 1, 6, 7, 0]
        [5, 8, 0, 0, 0, 0, 0, 0, 3]
        [0, 3, 0, 0, 2, 9, 0, 0, 0]