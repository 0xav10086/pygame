import numpy as np

def life_game(board, steps):
    def get_neighbors(r, c):
        rows = len(board)
        cols = len(board[0])
        neighbors = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == dc == 0:
                    continue
                rr = r + dr
                cc = c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    neighbors += board[rr][cc]
        return neighbors

    for step in range(steps):
        new_board = np.zeros_like(board)
        for r in range(len(board)):
            for c in range(len(board[0])):
                n = get_neighbors(r, c)
                if board[r][c] == 1 and n in [2, 3]:
                    new_board[r][c] = 1
                elif board[r][c] == 0 and n == 3:
                    new_board[r][c] = 1
        board = new_board
        print(f'Step {step + 1}:')
        print(board)

        # Check if the board is all zeros and display a message
        if np.sum(board) == 0:
            print("This world fell into silence. All cells are dead.")
            return board

    return board

def generate_random_board(rows, cols, steps):
    while True:
        # Generate a random board
        board = np.random.choice([0, 1], size=(rows, cols), p=[0.5, 0.5])
        # Simulate the game for the specified number of steps
        result = life_game(board.copy(), steps)
        # Check if the resulting board is not all zeros (i.e. not all cells are dead)
        if np.sum(result) > 0:
            # Return the generated random board
            return board

# Get user input for the number of steps
while True:
    try:
        steps = int(input("Enter the number of steps: "))
        if steps <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Provide instructions for entering the board
print("Enter the board as a string of 0s and 1s, separated by spaces.")
print("Alternatively, enter 'life' to generate a random non-dead environment.")
board_str = input("Enter the board: ")

# Check if the user entered 'life' to generate a random non-dead environment
if board_str.lower() == 'life':
    # Generate a random non-dead environment with size 12x12 that will not die within the specified number of steps
    board = generate_random_board(12, 12, steps)

else:
    # Convert user input to a 2D NumPy array
    board = np.fromstring(board_str, sep=' ').reshape(-1, int(np.sqrt(len(board_str.split()))))

# If the input board is smaller than 12x12, pad it to 12x12
if board.shape[0] < 12 or board.shape[1] < 12:
    new_board = np.zeros((12, 12), dtype=int)
    new_board[:board.shape[0], :board.shape[1]] = board
    board = new_board

# Run the Game of Life simulation
result = life_game(board, steps)

# Output the final result
print('Final result:')
print(result)
