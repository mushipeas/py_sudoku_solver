#!/usr/bin/env python3

__version__ = "0.1"
__author__ = "Muj Zaidi"
__all__ = ["solve", "printable_grid"]

from itertools import combinations, chain

MAX_ITERATIONS = 100000


def solve(partial_grid: list) -> list:
    """Backtracking solver for a sudoku grid, passed in as any 81 length iterable of strings or numbers.
    Empty items must be none or empty strings / lists.
    Any element outside of the 1-9 range will be replaced with None.
    Returns solved grid, as a list of len 81 if solvable.
    Returns None if MAX_ITERATIONS is exceeded.
    """
    original_grid = [int(x) if x and int(x) < 10 and int(x) > 0 else None for x in partial_grid]
    grid = list(original_grid)

    i = 0
    iterations = 0

    while i >= 0 and i < 81:
        iterations += 1

        if iterations >= MAX_ITERATIONS:
            break

        if not grid[i]:
            grid[i] = 1

        if grid[i] > 9:
            grid[i] = None
            i -= 1
            while original_grid[i] and i:
                i -= 1
            grid[i] += 1

        if conditions_met(grid, i) and grid[i] <= 9:
            i += 1
            while i < 81 and original_grid[i]:
                i += 1
        else:
            grid[i] += 1
    else:
        print("Solution required {} iterations.".format(iterations))
        return grid
    return None

# no longer needed
def all_conditions_met(grid) -> bool:
    """Checks (lazy) if the grid fails any of the 27 conditions:
    - No recurring numbers in any row or column (18)
    - No recurring numbers in any 'square' region (9)
    False if any condition fails, True otherwise.
    """
    for i in range(9):
        if duplicates(grid[row(i)]) or duplicates(grid[col(i)]) or duplicates(square(grid, i)):
            return False
    else:
        return True


def conditions_met(grid, index) -> bool:
    """Checks (lazy) if the grid fails any of the 3 of 27 conditions relevant
    to the element(index) of the grid:
    - No recurring numbers in any row or column (2 of 18)
    - No recurring numbers in any 'square' region (1 of 9)
    False if any condition fails, True otherwise.
    """
    i, j, k = calc_subgroup_indices(index)

    if duplicates(grid[row(i)]) or duplicates(grid[col(j)]) or duplicates(square(grid, k)):
        return False
    else:
        return True


def calc_subgroup_indices(index) -> (int, int, int):
    """Returns the row, col and square indices
    that the element at (index) is part of.
    """
    row_i = index // 9
    col_i = index % 9
    sqr_i = row_i//3 * 3 + col_i//3
    return row_i, col_i, sqr_i


def duplicates(group) -> bool:
    """Checks input for duplicates (not inc. Nones)."""
    group = (x for x in group if x)
    for x, y in combinations(group, 2):
        if x == y:
            return True
    return False


def row(row_no) -> slice:
    """Returns slice object for appropriate row.
    Note: Can this be memoised? Would it help in any way?
    """
    start = 0 + row_no * 9
    stop = 9 + row_no * 9
    return slice(start, stop)


def col(col_no) -> slice:
    """Returns slice object for appropriate column.
    Note: Can this be memoised? Would it help in any way?
    """
    start = col_no
    step = 9
    return slice(start, None, step)


def square(grid, sq_no) -> object:
    """Returns generator for values in given square region."""
    return (grid[i] for i in square_indices(sq_no))


def square_indices(sq_no) -> list:
    """Returns element index numbers for appropriate section on grid."""
    indices = (x + sq_no%3 * 3 + sq_no//3 * 27 + row * 9 for row in range(3)
                                                            for x in range(3))
    return indices


def printable_grid(grid) -> list:
    """Reshapes 'grid' from 81x1 to 9x9 for printing."""
    square_grid = []
    for i in range(9):
        line = [x if x else 0 for x in grid[row(i)]]
        square_grid.append(line)

    return square_grid


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=
        """Backtracking iterative solver for a sudoku grid.
        Prints the solved grid, if successful. Otherwise states not solvable.
        """)
    parser.add_argument(
        "GRID", help=
        """String representing unsolved grid of len(81).
        Empties must be given as 0's.
        Spaces, commas and brackets will be ignored.
        ie. '[1,2,0,5...3,5]' or '1205...35'.
        """,
        type=list)
    args = parser.parse_args()

    try:
        grid = [int(x) for x in args.GRID if x not in "[ ,]"]
    except ValueError:
        print("Please review input argument. See help for syntax.")
    else:
        print("Input read as:")
        print(*printable_grid(grid), sep="\n")
        try:
            solved_grid = solve(grid)
        except (IndexError, TypeError):
            print("Grid is unsolvable. Please check the input again.")
        else:
            print("Solved!")
            print(*printable_grid(solved_grid), sep="\n")