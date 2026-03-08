import time
from helpers import load_puzzles_from_file, load_board_from_string, get_default_board

# Step counter
steps = 0
show_progress = False

# Loop every row
def print_board(board):
    for i in range(len(board)):
        # Every 3 rows, print a horizontal line
        if i % 3 == 0 and i != 0:
            print("-" * 21)
            
        # Loop every column in the row
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                # Every 3 column, print a vertical separator
                print("|", end=" ")
            # Print a number in that position
            value = board[i][j]
            print("." if value == 0 else value, end=" ")
            
        print()

# Looks for a empty first cell
def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid(board, num, pos):
    row, col = pos
    
    #Check row
    for j in range(9):
        if board[row][j] == num and j != col:
            return False
        
    #Check column
    for i in range(9):
        if board[i][col] == num and i != row:
            return False
        
    #Check 3x3 box
    box_row = row // 3
    box_col = col // 3
    
    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
        
    return True

def get_candidates(board, row, col):
    candidates = []
    
    if board[row][col] != 0:
        return candidates
    
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            candidates.append(num)
            
    return candidates

def find_best_empty(board):
    best_pos = None
    best_candidates = None
    
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                candidates = get_candidates(board, row, col)
                
                if best_candidates is None or len(candidates) < len(best_candidates):
                    best_pos = (row, col)
                    best_candidates = candidates
                    
                    # Early exit, best possible case
                    if len(best_candidates) == 1:
                        return best_pos
                    
    return best_pos

def solve(board):
    global steps
    
    # Looks for a first empty cell
    empty = find_best_empty(board)
    
    # If none is empty, the puzzle is done
    if empty is None:
        return True
    
    # Take the empty position
    row, col = empty
    
    # Try number 1 - 9
    for num in range(1, 10):
        
        # Count steps
        steps += 1
        
        # Print progress every 1000 steps
        if show_progress and steps % 1000 == 0:
            print(f"\nStep {steps}")
            
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            
            if solve(board):
                return True
            
            # Reset
            board[row][col] = 0
            
    return False

def main():
    global steps
    
    # Load puzzles from file
    puzzles = load_puzzles_from_file("puzzles.txt")
    
    # If no puzzles are found, fallback to the default board
    if not puzzles:
        print("No valid puzzles found in puzzles.txt")
        print("Using default board instead.\n")
        
        default_board = get_default_board
        
        # Convert default board into puzzle string format
        default_puzzle = ""
        for row in default_board:
            for num in row:
                default_puzzle += str(num)
                
    print(f"Loaded {len(puzzles)} puzzle(s)\n")
    
    # Statistics
    solved_count = 0
    failed_count = 0
    total_time = 0
    
    # Solve each puzzle in the file
    for i, puzzle in enumerate(puzzles):
        
        # Reset step counter for each puzzle
        steps = 0
        
        # Convert puzzle string into a 9 x 9 board
        board = load_board_from_string(puzzle)
        
        start_time = time.time()
        
        # For the first puzzle, show the board before solving
        if i == 0:
            print("=" * 10 + " Puzzle 1 " + "=" * 10)
            print("\nSudoku before solving:\n")
            print_board(board)
            print()
            
        # Solve the puzzle using backtracking
        solved = solve(board)
        
        end_time = time.time()
        elapsed = end_time - start_time
        total_time += elapsed
        
        # Updated statistics
        if solved:
            solved_count += 1
        else:
            failed_count += 1
            
        # Show detailed output for the first puzzle
        if i == 0:
            if solved:
                print("Sudoku solved:\n")
                print_board(board)
            else:
                print("No solution exists.")
                
            print(f"\nAttempts: {steps}")
            print(f"Time: {elapsed:.6f} seconds\n")
            
        # For the rest of the puzzles, show summary only
        else:
            status = "solved" if solved else "failed"
            print(f"Puzzle {i+1}: {status} | Attemps: {steps} | Time: {elapsed:.6f}s")
            
    # Print final summary
    print("\n" + "=" * 10 + " Summary " + "=" * 10)
    print(f"Solved      : {solved_count}")
    print(f"Failed      : {failed_count}")
    print(f"Total time  : {total_time:.6f} seconds")
    
if __name__ == "__main__":
    main()