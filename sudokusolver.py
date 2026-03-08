from helpers import load_puzzles_from_file, load_board_from_string, get_default_board

# Input your puzzles in the puzzles.txt file
puzzles = load_puzzles_from_file("puzzles.txt")

if puzzles:
    board = load_board_from_string(puzzles[0])
else:
    print("No valid puzzles found in puzzles.txt")
    board = get_default_board()

# Step counter
steps = 0
debug = False

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
            print(board[i][j], end=" ")
            
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

def solve(board):
    global steps
    
    # Looks for a first empty cell
    empty = find_empty(board)
    
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
        if debug and steps % 1000 == 0:
            print(f"\nStep {steps}")
            
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            
            if solve(board):
                return True
            
            # Reset
            board[row][col] = 0
            
    return False

print("Sudoku before solving:\n")
print_board(board)

if solve(board):
    print("\nSudoku solved:\n")
    print_board(board)
    print(f"\nSolved in {steps} attempts.")
else:
    print("No solution exists.")