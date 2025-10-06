import tkinter as tk
from tkinter import messagebox

# --- CSP-Based Sudoku Solver ---

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


# --- GUI Section ---

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver (CSP Version)")
        self.entries = [[tk.Entry(root, width=2, font=("Arial", 20), justify="center") for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                e = self.entries[i][j]
                e.grid(row=i, column=j, padx=2, pady=2)
                # Add visual box borders
                if (j+1) % 3 == 0 and j != 8:
                    e.grid(padx=(2, 8))
                if (i+1) % 3 == 0 and i != 8:
                    e.grid(pady=(2, 8))

        # Buttons
        tk.Button(root, text="Solve (CSP)", command=self.solve, bg="lightgreen", font=("Arial", 14)).grid(row=9, column=0, columnspan=4, sticky="we", pady=5)
        tk.Button(root, text="Clear", command=self.clear, bg="lightcoral", font=("Arial", 14)).grid(row=9, column=5, columnspan=4, sticky="we", pady=5)

    def get_grid(self):
        """Get Sudoku grid from input fields."""
        grid = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                row.append(int(val) if val.isdigit() else 0)
            grid.append(row)
        return grid

    def set_grid(self, grid):
        """Display Sudoku grid on GUI."""
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if grid[i][j] != 0:
                    self.entries[i][j].insert(0, str(grid[i][j]))

    def solve(self):
        grid = self.get_grid()
        if solve_csp(grid):
            self.set_grid(grid)
            messagebox.showinfo("Sudoku Solver", "Solved successfully!")
        else:
            messagebox.showinfo("Sudoku Solver", "No solution found!")

    def clear(self):
        """Clear the grid."""
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)


# --- Run the GUI ---
root = tk.Tk()
SudokuGUI(root)
root.mainloop()
