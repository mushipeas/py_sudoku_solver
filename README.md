# `py_sudoku_solver`

A brute-force sudoku solver, using iteration and backtracking.

By using iteration, we can avoid any need for tail-call optimisation in a recursive solution.

Written for and tested on Python 3.7.5

## Running from cmd-line:

### Usage
    usage: py_sudoku_solver.py [-h] GRID

    Backtracking iterative solver for a sudoku grid.
    Prints the solved grid, if successful. Otherwise states not solvable.

    positional arguments:
    GRID        String representing unsolved grid of len(81). Empties must be
                given as 0's. Spaces, commas and brackets will be ignored.
                ie. '[1,2,0,5...3,5]' or '1205...35'


### Example
    >python py_sudoku_solver.py "[2, 0, 9, 0, 8, 0, 5, 0, 0, 0, 0, 4, 7, 6, 9, 0, 0, 0, 3, 0, 0, 0, 1, 2, 0, 4, 0, 0, 0, 3, 6, 0, 0, 0, 5, 
    4, 0, 4, 0, 0, 0, 0, 0, 8, 0, 8, 5, 0, 0, 0, 7, 6, 0, 0, 0, 2, 0, 8, 7, 0, 0, 0, 9, 0, 0, 0, 1, 9, 6, 2, 0, 0, 0, 0, 5, 0, 4, 0, 1, 0, 8]"
    Input read as:
    [2, 0, 9, 0, 8, 0, 5, 0, 0]
    [0, 0, 4, 7, 6, 9, 0, 0, 0]
    [3, 0, 0, 0, 1, 2, 0, 4, 0]
    [0, 0, 3, 6, 0, 0, 0, 5, 4]
    [0, 4, 0, 0, 0, 0, 0, 8, 0]
    [8, 5, 0, 0, 0, 7, 6, 0, 0]
    [0, 2, 0, 8, 7, 0, 0, 0, 9]
    [0, 0, 0, 1, 9, 6, 2, 0, 0]
    [0, 0, 5, 0, 4, 0, 1, 0, 8]
    Solution required 2479 iterations
    Solved!
    [2, 6, 9, 3, 8, 4, 5, 1, 7]
    [5, 1, 4, 7, 6, 9, 8, 2, 3]
    [3, 8, 7, 5, 1, 2, 9, 4, 6]
    [1, 9, 3, 6, 2, 8, 7, 5, 4]
    [7, 4, 6, 9, 5, 1, 3, 8, 2]
    [8, 5, 2, 4, 3, 7, 6, 9, 1]
    [6, 2, 1, 8, 7, 5, 4, 3, 9]
    [4, 3, 8, 1, 9, 6, 2, 7, 5]
    [9, 7, 5, 2, 4, 3, 1, 6, 8]

## Useage as part of a module:

### solve()
The main function in the script is `solve()` which takes an iterable of the sudoku elements as an input, and returns a completed list.

    py_soduku_solver.solve(grid: iter) -> solved_grid: list

The input should be of len 81 to represent a sudoku board, in the order [[r0,c0], [r0,c1] ...[r8,c8]].

Empty items in the input must be `None` or empty strings / lists.
Any element outside of the 1-9 range will also be replaced with `None` by the function.

### print_grid()
The `printable_grid()` function can generate the list in a more viewable form:

    py_soduku_solver.printable_grid(grid: iter) -> list[lists]

Useable as:

    print(*printable_grid(grid), sep='\n')

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