import random

# Initialize the Tic Tac Toe board
board = [' ' for _ in range(9)]

# Function to print the Tic Tac Toe board
def print_board():
    print(' | '.join(board[:3]))
    print('-' * 9)
    print(' | '.join(board[3:6]))
    print('-' * 9)
    print(' | '.join(board[6:9]))

# Function to check if the board is full
def is_board_full():
    return ' ' not in board

# Function to check if a player has won
def check_winner(player):
    # Check rows, columns, and diagonals
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to make a player's move
def make_move(player, position):
    if board[position] == ' ':
        board[position] = player

# Function for computer's move (random)
def computer_move():
    empty_cells = [i for i, cell in enumerate(board) if cell == ' ']
    if empty_cells:
        random_move = random.choice(empty_cells)
        make_move('O', random_move)

# Main game loop
def main():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        # Player X's turn
        while True:
            x_move = int(input("Player X, enter your move (1-9): ")) - 1
            if 0 <= x_move <= 8:
                if board[x_move] == ' ':
                    make_move('X', x_move)
                    break
                else:
                    print("Invalid move. The cell is already occupied.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        
        print_board()
        if check_winner('X'):
            print("Player X wins!")
            break
        if is_board_full():
            print("It's a tie!")
            break
        
        # Computer's turn
        computer_move()
        print_board()
        if check_winner('O'):
            print("Computer wins!")
            break
        if is_board_full():
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
