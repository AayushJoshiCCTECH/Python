# Tic Tac Toe – Python CLI Game

A simple **command-line Tic Tac Toe game** built using Python. This project focuses on **clean input validation**, **game logic clarity**, and **beginner-friendly structure**, making it perfect for learning and interviews.

---

## Features

* Two-player game (`X` vs `O`)
* Interactive CLI input
* Input validation (no crashes on wrong input)
* Detects **win** and **draw** conditions
* Shows a **reference board** (1–9) before the game starts
* Prints the **updated board after every move**

---

## How the Game Works

1. The game first displays a **reference board** with positions `1` to `9`.
2. Players take turns entering a number between `1` and `9`.
3. The chosen position is marked with the current player's symbol (`X` or `O`).
4. After every move:

   * The updated board is printed
   * The game checks for a **winner** or a **draw**
5. The game ends when a player wins or the board is full.

---

## Board Position Reference

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

---

## Input Validation Logic

The game safely handles:

* Non-numeric input (e.g. `a`, `@`, empty input)
* Numbers outside the range `1–9`
* Attempts to play on an already occupied position

This is achieved using:

* `try-except` blocks for safe integer conversion
* Explicit range and board checks

---

## How to Run

1. Make sure Python **3.14.0** is installed
2. Save the game code as `tic_tac_toe.py`
3. Run the game:

```bash
python tic_tac_toe.py
```

---

## Project Structure

```
TicTacToe/
│
├── tic_tac_toe.py   # Main game logic
└── README.md        # Project documentation
```

---

## Concepts Covered

* Python loops (`while True`)
* Conditional expressions (ternary operator)
* Exception handling (`try-except`)
* Functions and modular code
* Lists and indexing
* Basic game state management

---

## Possible Enhancements

* Convert the game to **OOP (class-based)** design
* Add a **single-player AI** mode
* Add **replay** functionality
* Add **unit tests**
* Improve CLI visuals

---

##  Author

**Aayush Joshi**
Learning Python step-by-step through hands-on projects.

---

Happy coding! 
