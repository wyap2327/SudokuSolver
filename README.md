# Sudoku Solver  

A **Sudoku solver** implemented using **Constraint Satisfaction Problems (CSP)**.  

## How it Works  
Sudoku can be represented as a **CSP** defined by the tuple:  

**CSP = (X, D, C)**  

- **X** → Set of variables – the 9×9 Sudoku grid (81 cells)  
- **D** → Set of domains – possible values for each variable (1–9)  
- **C** → Set of constraints – rules that restrict which values can be placed in each cell  

By modeling Sudoku as a CSP, the solver applies **constraint propagation** and **search techniques** to efficiently find valid solutions.  
