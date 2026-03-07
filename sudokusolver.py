board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Loop every boards
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
    # Looks for a first empty cell
    empty = find_empty(board)
    
    # If none is empty, the puzzle is done
    if empty is None:
        return True
    
    # Take the empty position
    row, col = empty
    
    # Try number 1 - 9
    for num in range(1, 10):
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
else:
    print("No solution exists.")