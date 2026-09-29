try:
    from termcolor import colored
except ImportError:
    def colored(text, color):
        return text


X = "X"
O = "O"
EMPTY = " "


def new_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]


def show_mark(mark):
    if mark == X:
        return colored(mark, "red")
    elif mark == O:
        return colored(mark, "green")
    return mark


def display_board(board):
    print("\n")
    for r in range(3):
        row = " | ".join(show_mark(cell) for cell in board[r])
        print(f" {row} ")
        if r < 2:
            print("---+---+---")
    print()


def get_coordinates(position):
    position -= 1
    return position // 3, position % 3


def winner(board, player):
    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def board_full(board):
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def get_move(board):
    while True:
        choice = input("Choose a position (1-9): ").strip()

        if not choice.isdigit():
            print("Please enter a number between 1 and 9.")
            continue

        pos = int(choice)

        if pos < 1 or pos > 9:
            print("Position must be between 1 and 9.")
            continue

        row, col = get_coordinates(pos)

        if board[row][col] != EMPTY:
            print("That position is already occupied.")
            continue

        return row, col


def play():
    board = new_board()
    current = X

    print("\nTIC-TAC-TOE")
    print("\nBoard Layout:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:
        display_board(board)

        print(f"Player {show_mark(current)} turn")
        row, col = get_move(board)
        board[row][col] = current

        if winner(board, current):
            display_board(board)
            print(f"Player {show_mark(current)} wins!")
            break

        if board_full(board):
            display_board(board)
            print("Match Draw!")
            break

        current = O if current == X else X


def main():
    while True:
        play()

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()