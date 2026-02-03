from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Game state
board = [' '] * 9
current_player = "X"


def check_winner(player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)


def is_draw():
    return all(cell in ["X", "O"] for cell in board)


@app.route("/", methods=["GET", "POST"])
def index():
    global current_player

    message = ""

    if request.method == "POST":
        move = request.form.get("move")

        if move and move.isdigit():
            move = int(move)

            if 0 <= move < 9 and board[move] == ' ':
                board[move] = current_player

                if check_winner(current_player):
                    message = f"Player {current_player} wins!"
                elif is_draw():
                    message = "It's a draw!"
                else:
                    current_player = "O" if current_player == "X" else "X"


    return render_template(
        "index.html",
        board=board,
        current_player=current_player,
        message=message
    )


@app.route("/reset")
def reset():
    global board, current_player
    board = [' '] * 9
    current_player = "X"
    return redirect(url_for("index"))



if __name__ == "__main__":
    # IMPORTANT: allows LAN access
    app.run()
