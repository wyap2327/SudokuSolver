def is_valid(grid, r, c, k):
    """Check if putting k at (r, c) is valid under Sudoku rules."""
    not_in_row = k not in grid[r]
    not_in_column = k not in [grid[i][c] for i in range(9)]
    not_in_box = k not in [grid[i][j] for i in range(r//3*3, r//3*3+3)
                           for j in range(c//3*3, c//3*3+3)]
    return not_in_row and not_in_column and not_in_box


def find_unassigned_with_mrv(grid):
    """Find the cell with the fewest possible valid numbers (MRV heuristic)."""
    best_cell = None
    min_possibilities = 10  # higher than max (9)
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                # compute possible values
                possibilities = [k for k in range(1, 10) if is_valid(grid, r, c, k)]
                if len(possibilities) < min_possibilities:
                    min_possibilities = len(possibilities)
                    best_cell = (r, c, possibilities)
    return best_cell


def solve_csp(grid):
    """Solve Sudoku using backtracking + MRV + forward checking."""
    cell = find_unassigned_with_mrv(grid)
    if not cell:
        return True  # solved

    r, c, possibilities = cell

    for k in possibilities:
        if is_valid(grid, r, c, k):
            grid[r][c] = k
            if solve_csp(grid):
                return True
            grid[r][c] = 0  # backtrack
    return False


# Example puzzle
grid = [
    [0, 0, 4, 0, 5, 0, 0, 0, 0],
    [9, 0, 0, 7, 3, 4, 6, 0, 0],
    [0, 0, 3, 0, 2, 1, 0, 4, 9],
    [0, 3, 5, 0, 9, 0, 4, 8, 0],
    [0, 9, 0, 0, 0, 0, 0, 3, 0],
    [0, 7, 6, 0, 1, 0, 9, 2, 0],
    [3, 1, 0, 9, 7, 0, 2, 0, 0],
    [0, 0, 9, 1, 8, 2, 0, 0, 3],
    [0, 0, 0, 0, 6, 0, 1, 0, 0]
]

solve_csp(grid)
print(*grid, sep='\n')
