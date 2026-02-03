from flask import Flask, render_template, request, redirect, url_for
from flask import session

app = Flask(__name__)

app.secret_key = "tictactoe-secret"

# Game state
board = [' '] * 9
current_player = "X"


def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)


def is_draw(board):
    return all(cell in ["X", "O"] for cell in board)



@app.route("/", methods=["GET", "POST"])
def index():

    if "board" not in session:
        session["board"] = [' '] * 9
        session["current_player"] = "X"

    board = session["board"]
    current_player = session["current_player"]
    message = ""

    if request.method == "POST":
        move = request.form.get("move")

        if move and move.isdigit():
            move = int(move)

            if 0 <= move < 9 and board[move] == ' ':
                board[move] = current_player

                if check_winner(board, current_player):
                    message = f"Player {current_player} wins!"
                elif is_draw(board):
                    message = "It's a draw!"
                else:
                    session["current_player"] = "O" if current_player == "X" else "X"


        session["board"] = board

    return render_template(
        "index.html",
        board=board,
        current_player=session["current_player"],
        message=message
    )

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))




if __name__ == "__main__":
    # IMPORTANT: allows LAN access
    app.run()
