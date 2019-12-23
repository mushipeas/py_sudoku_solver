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
            if i < 81 and _original_grid[i]:
                i += 1

        else:
            _grid[i] += 1
    
    print("Solution required {} iterations".format(iterations))
    return _grid


def conditions_met(grid) -> bool:
    """
    Checks (lazy) if the grid fails any of the 27 conditions:
    - No recurring numbers in any line or column (18)
    - No recurring numbers in any square region (9)
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
    top_row = (x + sq_no%3 * 3 + sq_no//3 * 27 + row * 9 for row in range(3)
                                                            for x in range(3))

    return top_row

def print_grid(grid):
    """
    Prints the sudoku grid in a more readable format
    """
    for i in range(9):
        print(grid[row(i)])


if __name__ == "__main__":
    
    ##### ---------------- Test grids ---------------- #####    

    grid = [
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

        ### sol(grid) =
        #     [2, 6, 9, 3, 8, 4, 5, 1, 7]
        #     [5, 1, 4, 7, 6, 9, 8, 2, 3]
        #     [3, 8, 7, 5, 1, 2, 9, 4, 6]
        #     [1, 9, 3, 6, 2, 8, 7, 5, 4]
        #     [7, 4, 6, 9, 5, 1, 3, 8, 2]
        #     [8, 5, 2, 4, 3, 7, 6, 9, 1]
        #     [6, 2, 1, 8, 7, 5, 4, 3, 9]
        #     [4, 3, 8, 1, 9, 6, 2, 7, 5]
        #     [9, 7, 5, 2, 4, 3, 1, 6, 8]

    grid2 = [
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

        ### sol(grid2) =
        #     [3, 5, 9, 6, 7, 8, 1, 4, 2]
        #     [1, 7, 8, 2, 9, 4, 5, 3, 6]
        #     [6, 4, 2, 1, 5, 3, 7, 8, 9]
        #     [4, 2, 3, 7, 8, 5, 9, 6, 1]
        #     [8, 1, 5, 9, 4, 6, 3, 2, 7]
        #     [9, 6, 7, 3, 1, 2, 4, 5, 8]
        #     [2, 9, 4, 8, 3, 1, 6, 7, 5]
        #     [5, 8, 1, 4, 6, 7, 2, 9, 3]
        #     [7, 3, 6, 5, 2, 9, 8, 1, 4]

    ##### ---------------- Component tests ---------------- #####    

    group = {
        "l1" : range(10),                       # False
        "l2" : list('abcdefghi'),               # False
        "l3" : 'abcdwaeda',                     # True
        "l4" : list('abcdwaeda'),               # True
        "l5" : [1, 1, 4, 5, 6, None],           # True
        "l6" : [1, 2, 3, 4, 5, 6, None, None]   # False
    }

    for li in group.values():
        res = duplicates(li)
        print(res)

    print(row(0))                               # slice(0, 9, None)
    print(row(1))                               # slice(9, 18, None)
    print(row(8))                               # slice(72, 81, None)
    print(grid[row(1)])                         # [None, None, 4, 7, 6, 9, None, None, None]
    print(grid2[row(8)])                        # [None, 3, None, None, 2, 9, None, None, None]

    print(col(0))                               # slice(0, None, 9)
    print(col(1))                               # slice(1, None, 9)
    print(col(8))                               # slice(8, None, 9)
    print(grid[col(1)])                         # [None, None, None, None, 4, 5, 2, None, None]
    print(grid2[col(8)])                        # [None, 6, None, None, None, 8, None, 3, None]

    print(list(square_indexes(0)))              # [0, 1, 2, 9, 10, 11, 18, 19, 20]
    print(list(square_indexes(1)))              # [3, 4, 5, 12, 13, 14, 21, 22, 23]
    print(list(square_indexes(8)))              # [60, 61, 62, 69, 70, 71, 78, 79, 80]
    print(list(square(grid, 1)))                # [None, 8, None, 7, 6, 9, None, 1, 2]
    print(list(square(grid2, 4)))               # [7, None, None, None, None, None, None, None, 2]

    print(conditions_met(grid))                 # True


    ##### ---------------- Full tests ---------------- #####
    solved_grid = solve(grid)
    print_grid(solved_grid)

    solved_grid2 = solve(grid2)
    print_grid(solved_grid2)