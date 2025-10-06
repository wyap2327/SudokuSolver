import tkinter as tk
from tkinter import messagebox

# Sudoku Solver Functions
def is_valid(grid, r, c, k):
    not_in_row = k not in grid[r]
    not_in_column = k not in [grid[i][c] for i in range(9)]
    not_in_box = k not in [grid[i][j] for i in range(r//3*3, r//3*3+3) for j in range(c//3*3, c//3*3+3)]
    return not_in_row and not_in_column and not_in_box

def solve(grid, r=0, c=0):
    if r == 9:
        return True
    elif c == 9:
        return solve(grid, r+1, 0)
    elif grid[r][c] != 0:
        return solve(grid, r, c+1)
    else:
        for k in range(1, 10):
            if is_valid(grid, r, c, k):
                grid[r][c] = k
                if solve(grid, r, c+1):
                    return True
                grid[r][c] = 0
        return False

# GUI
class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.cells = [[tk.Entry(root, width=2, font=("Arial", 24), justify="center") for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.cells[i][j].grid(row=i, column=j, padx=2, pady=2)
        
        # Solve button
        tk.Button(root, text="Solve", command=self.solve_puzzle, bg="lightgreen", font=("Arial", 14)).grid(row=9, column=0, columnspan=4, sticky="we")
        # Clear button
        tk.Button(root, text="Clear", command=self.clear_grid, bg="lightcoral", font=("Arial", 14)).grid(row=9, column=5, columnspan=4, sticky="we")

    def get_grid(self):
        grid = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.cells[i][j].get()
                row.append(int(val) if val.isdigit() else 0)
            grid.append(row)
        return grid

    def solve_puzzle(self):
        grid = self.get_grid()
        if solve(grid):
            for i in range(9):
                for j in range(9):
                    self.cells[i][j].delete(0, tk.END)
                    self.cells[i][j].insert(0, str(grid[i][j]))
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists!")

    def clear_grid(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)

# Run GUI
root = tk.Tk()
gui = SudokuGUI(root)
root.mainloop()