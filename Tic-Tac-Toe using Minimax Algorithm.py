# Tic-Tac-Toe using Minimax Algorithm

board = [" " for _ in range(9)]

# Display the board
def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Check winner
def check_winner():
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None

# Minimax algorithm
def minimax(is_maximizing):
    result = check_winner()

    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "Draw":
        return 0

    if is_maximizing:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score

# Find best move for AI
def best_move():
    best_score = -float("inf")
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move

# Main game
print("TIC-TAC-TOE")
print("You are X")
print("AI is O")

while True:
    display_board()

    # Human move
    position = int(input("Enter position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid move! Try again.")
        continue

    board[position] = "X"

    result = check_winner()

    if result:
        display_board()
        if result == "Draw":
            print("Game Draw!")
        else:
            print(result, "wins!")
        break

    # AI move
    ai_position = best_move()
    board[ai_position] = "O"

    print("AI selected position:", ai_position + 1)

    result = check_winner()

    if result:
        display_board()
        if result == "Draw":
            print("Game Draw!")
        else:
            print(result, "wins!")
        break
