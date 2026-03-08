# Sudoku Solver (Python)

A Sudoku solver implemented in Python using **recursive backtracking**.  
The solver was later optimized using the **Minimum Remaining Value (MRV) heuristic** to reduce the search space and improve performance.

## Features

- Recursive backtracking solver
- Sudoku constraint validation (row, column, 3×3 box)
- Multi-puzzle solving from `puzzles.txt`
- Step counter (number of search attempts)
- Execution time measurement
- MRV heuristic optimization

## Puzzle Format

Each puzzle must be written as **81 digits in a single line**.

Example (`puzzles.txt`):
530070000600195000098000060800060003400803001700020006060000280000419005000080079
600120384008459072000006005000264030070080006940003000310000050089700000502000190


`0` represents an empty cell.

## Run the Solver

From the project directory:

```bash
python main.py
```
The solver will:
- load puzzles from puzzles.txt
- solve them sequentially
- display the first puzzle in detail
- show summary results for the rest

## Example Output

Loaded 3 puzzle(s)

========== Puzzle 1 ==========

Sudoku before solving:

5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
---------------------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
---------------------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9

Attempts : 37652
Time     : 0.012431 seconds

Puzzle 2 | solved | Attempts: 18211 | Time: 0.006812s
Puzzle 3 | solved | Attempts: 22104 | Time: 0.008214s

## Optimization

Applying the MRV heuristic significantly reduces the search space.
Example improvement on harder puzzles:

Basic backtracking : ~2,000,000 attempts
MRV heuristic      : ~7,000 attempts
