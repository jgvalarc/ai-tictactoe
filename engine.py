import random
import time

BOARD_WIDTH = 3
BOARD_HEIGHT = 3

def new_board():
    board = []
    for x in range(0, BOARD_WIDTH):
        column = []
        for y in range(0, BOARD_HEIGHT):
            column.append(None)
        board.append(column)
    return board

def render(board):
    print("  0 1 2 ")
    print("  ------")
    for y in range(BOARD_HEIGHT):
        row = ''.join(board[x][y] if board[x][y] is not None else ' ' for x in range(BOARD_WIDTH))
        print(f"{y}|{' '.join(row)}|")
    print("  ------")

def get_move():
    while True:
        try:
            x = int(input("What is your move's X co-ordinate? (0-2): "))
            y = int(input("What is your move's Y co-ordinate? (0-2): "))
            
            # Ensure the coordinates are within the valid range
            if 0 <= x < BOARD_WIDTH and 0 <= y < BOARD_HEIGHT:
                return (x, y)
            else:
                print("Coordinates must be between 0 and 2. Please try again.")
        except ValueError:
            print("Invalid input. Please enter integers for X and Y coordinates.")

def make_move(board, player, move_coords):
    x, y = move_coords  # Unpack the coordinates

    # Check if the move is valid
    if board[x][y] is not None:
        raise Exception("Illegal move! The cell is already occupied.")
    
    # Update the board
    board[x][y] = player
    return board

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell is None:
                return False
    return True

def get_winner(board):
    # Check rows, columns, and diagonals
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    
    for col in range(BOARD_WIDTH):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None

# AI Algorithms

import random

# Ensure BOARD_WIDTH and BOARD_HEIGHT are defined somewhere in your program
BOARD_WIDTH = 3
BOARD_HEIGHT = 3

def random_ai(board):
    # Collect all available (legal) moves where the board position is None
    available_moves = [(x, y) for x in range(BOARD_WIDTH) for y in range(BOARD_HEIGHT) if board[x][y] is None]
    
    # Ensure that there is at least one valid move before choosing randomly
    if available_moves:
        return random.choice(available_moves)
    else:
        raise Exception("No available moves!")  # Shouldn't happen if the board is not full

def winning_ai(board):
    # Collect all available moves
    available_moves = [(x, y) for x in range(BOARD_WIDTH) for y in range(BOARD_HEIGHT) if board[x][y] is None]
    
    # Check if the AI can win in any of the available moves
    for move in available_moves:
        x, y = move
        board[x][y] = 'O'  # Simulate the AI's move
        if get_winner(board) == 'O':  # Check if this move wins the game
            board[x][y] = None  # Undo the move
            return move  # Return winning move
        board[x][y] = None  # Undo the move if no win found
    
    # If no winning move found, return a legal (random) move
    return random.choice(available_moves) if available_moves else None

def best_ai(board):
    # Collect all available moves
    available_moves = [(x, y) for x in range(BOARD_WIDTH) for y in range(BOARD_HEIGHT) if board[x][y] is None]
    
    # 1. Check for winning move
    for move in available_moves:
        x, y = move
        board[x][y] = 'O'  # Simulate AI's move
        if get_winner(board) == 'O':  # If AI wins
            board[x][y] = None  # Undo the move
            return move  # Return winning move
        board[x][y] = None  # Undo the move if no win found

    # 2. Block opponent's winning move
    for move in available_moves:
        x, y = move
        board[x][y] = 'X'  # Simulate opponent's move
        if get_winner(board) == 'X':  # If opponent wins
            board[x][y] = None  # Undo the move
            return move  # Return blocking move
        board[x][y] = None  # Undo the move if no block needed

    # 3. If no winning or blocking move found, return a random legal move
    return random.choice(available_moves) if available_moves else None



# AI vs AI Mode
def ai_vs_ai(ai1, ai2):
    board = new_board()
    player_turn = 'X'  # Player X starts
    
    while True:
        render(board)
        
        if player_turn == 'X':
            print("AI X's turn:")
            move_coords = ai1(board)  # AI X makes a move
        else:
            print("AI O's turn:")
            move_coords = ai2(board)  # AI O makes a move

        board = make_move(board, player_turn, move_coords)
        
        winner = get_winner(board)
        if winner:
            render(board)
            print(f"Player {winner} wins!")
            break

        if is_board_full(board):
            render(board)
            print("It's a draw!")
            break

        # AI Turn Delay
        time.sleep(3)  # Delay of 3 seconds between AI turns

        # Switch player turn
        player_turn = 'O' if player_turn == 'X' else 'X'

# Game Loop
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    
    # Choose game mode
    game_mode = input("Do you want to play against AI, another player, or AI vs AI? (AI/Player/AIvAI): ").strip().lower()
    
    if game_mode == "ai":
        ai_choice = input("Choose AI difficulty (random, winning, best): ").strip().lower()
        ai_function = {
            "random": random_ai,
            "winning": winning_ai,
            "best": best_ai
        }.get(ai_choice, best_ai)  # Default to 'best' AI if input is invalid

        board = new_board()
        player_turn = 'X'  # Player X starts
        
        while True:
            render(board)
            
            if player_turn == 'X':
                print(f"Player {player_turn}'s turn:")
                move_coords = get_move()  # Player's move
            else:
                print(f"AI ({player_turn})'s turn:")
                move_coords = ai_function(board)  # AI's move

            try:
                board = make_move(board, player_turn, move_coords)
            except Exception as e:
                print(e)
                continue

            winner = get_winner(board)
            if winner:
                render(board)
                print(f"Player {winner} wins!")
                break

            if is_board_full(board):
                render(board)
                print("It's a draw!")
                break

            # Switch player turn
            player_turn = 'O' if player_turn == 'X' else 'X'
    
    elif game_mode == "player":
        # Player vs Player mode, same as before
        board = new_board()
        player_turn = 'X'
        
        while True:
            render(board)
            
            print(f"Player {player_turn}'s turn:")
            move_coords = get_move()  # Player's move
            
            try:
                board = make_move(board, player_turn, move_coords)
            except Exception as e:
                print(e)
                continue
            
            winner = get_winner(board)
            if winner:
                render(board)
                print(f"Player {winner} wins!")
                break

            if is_board_full(board):
                render(board)
                print("It's a draw!")
                break

            # Switch player turn
            player_turn = 'O' if player_turn == 'X' else 'X'
    
    elif game_mode == "aivai":
        # AI vs AI mode
        ai1_choice = input("Choose AI X's difficulty (random, winning, best): ").strip().lower()
        ai2_choice = input("Choose AI O's difficulty (random, winning, best): ").strip().lower()

        ai1 = {
            "random": random_ai,
            "winning": winning_ai,
            "best": best_ai
        }.get(ai1_choice, best_ai)

        ai2 = {
            "random": random_ai,
            "winning": winning_ai,
            "best": best_ai
        }.get(ai2_choice, best_ai)

        ai_vs_ai(ai1, ai2)
