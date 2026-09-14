def print_board(board):
    for i, row in enumerate(board):
        row_str = " "
        for j, value in enumerate(row):
            row_str += value
            if j < len(row) - 1:
                row_str += " | "

        print(row_str)

        if i < len(board) - 1:
            print("-----------")


def set_values(turn, board):
    while True:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if row < 0 or row > len(board) - 1:
            print("Invalid input. Please enter a valid row.")

        elif col < 0 or col > len(board[row]) - 1:
            print("Invalid input. Please enter a valid column.")

        elif board[row][col] != " ":
            print("That position is already taken. Please choose another position.")
        else:
            break

    board[row][col] = turn


def check_winner(board, turn):
    # Check rows
    for row in board:
        if all(cell == turn for cell in row):
            return True

    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == turn for row in range(len(board))):
            return True

    # Check diagonals
    if all(board[i][i] == turn for i in range(len(board))):
        return True
    if all(board[i][len(board) - 1 - i] == turn for i in range(len(board))):
        return True

    return False


board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

turn = "X"
turn_count = 0
print_board(board)

while turn_count < len(board) * len(board[0]):
    print()
    print(f"\nIt's {turn}'s turn.")
    set_values(turn, board)
    print_board(board)
    if check_winner(board, turn):
        print(f"\n{turn} wins!")
        break

    if turn == "X":
        turn = "O"
    else:
        turn = "X"

    turn_count += 1

if turn_count == len(board) * len(board[0]):
    print("\nIt's a draw!")
else:
    print("Game over! Thanks for playing.")
