print("Welcome to Tic Tac Toe!")

board = [' '] * 9
current_player = 'X'


def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print("\n")


def check_winner(player):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in winning_positions
    )


def is_draw():
    return ' ' not in board

   
def print_reference_board():
    print("\nPositions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("\n")

print_reference_board()

while True:
    try:
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

        if not (0 <= move < 9):
            raise ValueError

        if board[move] != ' ':
            print("That position is already taken.")
            continue

        board[move] = current_player

        print_board()

        if check_winner(current_player):
            print(f"Player {current_player} wins!")
            break

        if is_draw():
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")
    
    except EOFError:
        print('No input detected. Exiting the game...')
        break

    except KeyboardInterrupt:
        print('Game interrupted by user. Exiting...')
        break
