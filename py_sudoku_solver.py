#!/usr/bin/env python3
from itertools import combinations, chain

def solve(partial_grid: list) -> list:
    """
    Backtracking solver for a sudoku grid, passed in as any 81 length iterable of strings or numbers
    Empty items must be none or empty strings / lists
    Any element outside of the 1-9 range will be replaced with None
    Returns solved grid, as a list of len 81 if solvable, else None
    """
    _original_grid = [int(x) if x and int(x) < 10 and int(x) > 0 else None for x in partial_grid]
    _grid = list(_original_grid)

    i = 0
    iterations = 0

    while i >= 0 and i < 81:
        iterations += 1

        if not _grid[i]:
            _grid[i] = 1


        if _grid[i] > 9:
            _grid[i] = None
            i -= 1
            while _original_grid[i] and i:
                i -= 1
            _grid[i] += 1


        if conditions_met(_grid) and _grid[i] <= 9:
            i += 1
            while i < 81 and _original_grid[i]:
                i += 1

        else:
            _grid[i] += 1
    
    print("Solution required {} iterations".format(iterations))
    return _grid


def conditions_met(grid) -> bool:
    """
    Checks (lazy) if the grid fails any of the 27 conditions:
    - No recurring numbers in any row or column (18)
    - No recurring numbers in any 'square' region (9)
    False if any condition fails, True otherwise
    """
    for i in range(9):
        if duplicates(grid[row(i)]) or duplicates(grid[col(i)]) or duplicates(square(grid, i)):
            return False
    else:
        return True


def duplicates(group) -> bool:
    """
    Checks input for duplicates (not inc. Nones)
    """
    _group = (x for x in group if x)
    for x, y in combinations(_group, 2):
        if x == y:
            return True
    
    return False

def row(row_no) -> slice:
    """
    Returns slice object for appropriate row.
    Can this be memoised? Would it help in any way?
    """
    start = 0 + row_no * 9
    stop =  9 + row_no * 9
    return slice(start,stop)

def col(col_no) -> slice:
    """
    Returns slice object for appropriate column.
    Can this be memoised? Would it help in any way?
    """
    start = col_no
    step = 9
    return slice(start, None, step)

def square(grid, sq_no) -> object:
    """
    Returns generator for values in given square region
    """
    return (grid[i] for i in square_indexes(sq_no))

def square_indexes(sq_no) -> list:
    """
    returns index numbers for appropriate section on grid
    """
    indexes = (x + sq_no%3 * 3 + sq_no//3 * 27 + row * 9 for row in range(3)
                                                            for x in range(3))

    return indexes

def printable_grid(grid):
    """
    Regenerates the sudoku grid in a more readable format for printing
    """
    square_grid = []
    for i in range(9):
        line = [x if x else 0 for x in grid[row(i)]]
        square_grid.append(line)

    return square_grid

if __name__ == "__main__":
    pass