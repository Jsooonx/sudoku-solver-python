# Return a default sudoku board (if no custom puzzle is provided)
def get_default_board():
    return [
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

# Convert an 81 char puzzle string into a 9x9 sudoku board
def load_board_from_string(puzzle_string):
    
    # Validate length
    if len(puzzle_string) != 81:
        print("Puzzle must contain exactly 81 characters.")
        return None
    
    new_board = []
    index = 0
    
    for row in range(9):
        current_row = []
        for col in range(9):
            char = puzzle_string[index]
            
            if not char.isdigit():
                print("Puzzle must contain digits only.")
                return None
            
            current_row.append(int(char))
            index += 1
            
        new_board.append(current_row)
        
    return new_board

# Return a board from puzzle string, or fallback to default board
def get_board(puzzle_string = None):
    if puzzle_string is None:
        return get_default_board()
    
    loaded_board = load_board_from_string(puzzle_string)
    
    if loaded_board is None:
        print("Invalid custom puzzle. Using default board instead.")
        return get_default_board()
    
    return loaded_board

# Load multiple sudoku puzzles from a text file
def load_puzzles_from_file(filename):
    puzzles = []
    
    try:
        with open((filename), "r") as file:
            lines = file.readlines()
            
        for line in lines:
            puzzle = line.strip()
            
            if len(puzzle) == 81 and puzzle.isdigit():
                puzzles.append(puzzle)
            else:
                print(f"Skipping invalid puzzle: {puzzle}")
    
    # Handle case where file doesn't exist
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        
    return puzzles