import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

def ai_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = random.choice(players)

    while True:
        print_board(board)

        if turn == "X":
            row, col = map(int, input("Enter your move (row col): ").split())
        else:
            print("AI is thinking...")
            row, col = ai_move(board)

        if board[row][col] != " ":
            print("That position is already taken. Try again.")
            continue

        board[row][col] = turn

        if check_winner(board, turn):
            print_board(board)
            print(f"{turn} wins!")
            break

        if all([cell != " " for row in board for cell in row]):
            print_board(board)
            print("It's a draw!")
            break

        turn = "O" if turn == "X" else "X"

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
