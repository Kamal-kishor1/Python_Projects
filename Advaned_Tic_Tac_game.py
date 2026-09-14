import time
import os, sys


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def typewriter(text, speed=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def display_game():
    time.sleep(1)
    typewriter("Welcome to the Tic Tac Toe game!")
    time.sleep(1)
    print()
    typewriter("Game is starting...")
    time.sleep(1)
    typewriter("................................", 0.05)
    time.sleep(1)
    clear_screen()
    typewriter(
        "The game board is a 3x3 grid. Players take turns to place their symbol (X or O) in an empty cell."
    )
    clear_screen()


def print_board(board):
    # for i, row in enumerate(board):
    #     row_str = " "

    # Print column headers
    print("    1   2   3")
    for i, row in enumerate(board):
        row_str = str(i + 1) + " "  # Row number on the left

        for j, value in enumerate(row):
            if value == "X":
                row_str += "\033[1;31mX\033[0m"  # Red X
            elif value == "O":
                row_str += "\033[1;34mO\033[0m"  # Blue O
            else:
                row_str += value

            if j < len(row) - 1:
                row_str += " | "

        print(row_str)
        if i < len(board) - 1:
            print("-----------")


def set_values(turn, board):
    while True:
        try:
            row = int(input("Enter the row (1-2-3): "))
            col = int(input("Enter the column (1-2-3): "))

        except ValueError:
            time.sleep(1)
            typewriter("Invalid input. Please enter a valid number.")
            continue

        if row < 1 or row > len(board):
            time.sleep(1)
            typewriter("Invalid input. Please enter a valid row.")

        elif col < 1 or col > len(board[row - 1]):
            time.sleep(1)
            typewriter("Invalid input. Please enter a valid column.")

        elif board[row - 1][col - 1] != " ":
            time.sleep(1)
            typewriter(
                "That position is already taken. Please choose another position."
            )
        else:
            break

    board[row - 1][col - 1] = turn


def check_winner(board, turn):
    size = len(board)

    # Collect all possible winning lines
    lines = []

    # Rows
    lines.extend(board)

    # Columns
    for col in range(size):
        lines.append([board[row][col] for row in range(size)])

    # Diagonals
    lines.append([board[i][i] for i in range(size)])  # Top-left to bottom-right
    lines.append(
        [board[i][size - 1 - i] for i in range(size)]
    )  # Top-right to bottom-left

    # Check if any line is filled with the same symbol
    for line in lines:
        if all(cell == turn for cell in line):
            return True

    return False


def switch_turn(turn):
    return "O" if turn == "X" else "X"


def replay_game():
    while True:
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay == "y":
            clear_screen()
            return True
        elif replay == "n":
            return False
        else:
            typewriter("Invalid input. Please enter 'y' or 'n'.")


while True:
    # Set up the New Game
    clear_screen()
    display_game()
    turn = "X"  # Starting player
    turn_count = 0  # Count of turns taken
    board = create_board()
    print_board(board)  # Display the initial empty board
    winner_found = False  # Flag to track if a winner has been found

    # Game Loop
    while turn_count < 9:
        print()
        typewriter(f"Player {turn}'s turn.")
        set_values(turn, board)
        print_board(board)
        if check_winner(board, turn):
            typewriter(f"Player {turn} wins!")
            winner_found = True
            break

        turn = switch_turn(turn)
        turn_count += 1

    # Check for Draw
    if not winner_found and turn_count == 9:
        typewriter("It's a draw!")

    # Replay Option
    if not replay_game():
        typewriter("Thanks for playing! Goodbye.")
        break
