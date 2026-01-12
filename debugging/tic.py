#!/usr/bin/python3

def print_board(board):
    """Print the Tic-Tac-Toe board."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 9)

def check_winner(board, player):
    """
    Check if the specified player has won.
    
    Args:
        board: The 3x3 game board
        player: The player to check ("X" or "O")
    
    Returns:
        bool: True if the player has won, False otherwise
    """
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    """Check if all cells on the board are occupied."""
    return all(cell != " " for row in board for cell in row)

def get_valid_input(prompt):
    """
    Get a valid integer input from the user.
    
    Args:
        prompt: The input prompt message
    
    Returns:
        int: Valid integer between 0 and 2
    """
    while True:
        try:
            value = input(prompt)
            num = int(value)
            if 0 <= num <= 2:
                return num
            else:
                print("Please enter a number between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")

def tic_tac_toe():
    """Main Tic-Tac-Toe game loop."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves_count = 0
    
    print("Welcome to Tic-Tac-Toe!")
    print("Players take turns entering row and column numbers (0, 1, or 2)")
    
    while True:
        print(f"\nCurrent board:")
        print_board(board)
        
        # Get player's move
        print(f"\nPlayer {current_player}'s turn")
        row = get_valid_input("Enter row (0, 1, or 2): ")
        col = get_valid_input("Enter column (0, 1, or 2): ")
        
        # Check if the spot is available
        if board[row][col] != " ":
            print("That spot is already taken! Please choose another.")
            continue
        
        # Make the move
        board[row][col] = current_player
        moves_count += 1
        
        # Check for win
        if check_winner(board, current_player):
            print_board(board)
            print(f"\n🎉 Congratulations! Player {current_player} wins! 🎉")
            break
        
        # Check for draw
        if moves_count == 9:  # All spots filled (3x3 = 9)
            print_board(board)
            print("\n🤝 It's a draw! The board is full. 🤝")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
