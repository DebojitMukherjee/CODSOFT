import tkinter as tk
from tkinter import messagebox

# --------------------------
# Game Variables
# --------------------------

board = [" " for _ in range(9)]

human = "X"
ai = "O"

human_score = 0
ai_score = 0
draw_score = 0

win_combos = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

# --------------------------
# Helper Functions
# --------------------------

def check_winner(brd, player):
    for combo in win_combos:
        if all(brd[i] == player for i in combo):
            return True
    return False


def is_draw(brd):
    return " " not in brd


def update_scoreboard():
    score_label.config(
        text=f"Player: {human_score}    AI: {ai_score}    Draws: {draw_score}"
    )


# --------------------------
# Minimax Algorithm
# --------------------------

def minimax(brd, is_maximizing):

    if check_winner(brd, ai):
        return 1

    if check_winner(brd, human):
        return -1

    if is_draw(brd):
        return 0

    if is_maximizing:

        best_score = -float("inf")

        for i in range(9):
            if brd[i] == " ":
                brd[i] = ai

                score = minimax(brd, False)

                brd[i] = " "

                best_score = max(score, best_score)

        return best_score

    else:

        best_score = float("inf")

        for i in range(9):
            if brd[i] == " ":
                brd[i] = human

                score = minimax(brd, True)

                brd[i] = " "

                best_score = min(score, best_score)

        return best_score


# --------------------------
# AI Move
# --------------------------

def best_move():

    global ai_score, draw_score

    best_score = -float("inf")
    move = None

    for i in range(9):

        if board[i] == " ":

            board[i] = ai

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = ai
    buttons[move].config(text=ai)

    if check_winner(board, ai):

        ai_score += 1
        update_scoreboard()

        messagebox.showinfo(
            "Game Over",
            f"AI Wins!\n\n"
            f"Player: {human_score}\n"
            f"AI: {ai_score}\n"
            f"Draws: {draw_score}"
        )

        reset_game()
        return

    if is_draw(board):

        draw_score += 1
        update_scoreboard()

        messagebox.showinfo(
            "Game Over",
            f"It's a Draw!\n\n"
            f"Player: {human_score}\n"
            f"AI: {ai_score}\n"
            f"Draws: {draw_score}"
        )

        reset_game()


# --------------------------
# Human Move
# --------------------------

def player_move(index):

    global human_score, draw_score

    if board[index] != " ":
        return

    board[index] = human
    buttons[index].config(text=human)

    if check_winner(board, human):

        human_score += 1
        update_scoreboard()

        messagebox.showinfo(
            "Game Over",
            f"You Win!\n\n"
            f"Player: {human_score}\n"
            f"AI: {ai_score}\n"
            f"Draws: {draw_score}"
        )

        reset_game()
        return

    if is_draw(board):

        draw_score += 1
        update_scoreboard()

        messagebox.showinfo(
            "Game Over",
            f"It's a Draw!\n\n"
            f"Player: {human_score}\n"
            f"AI: {ai_score}\n"
            f"Draws: {draw_score}"
        )

        reset_game()
        return

    best_move()


# --------------------------
# Reset Game
# --------------------------

def reset_game():

    global board

    board = [" " for _ in range(9)]

    for btn in buttons:
        btn.config(text="")


# --------------------------
# GUI
# --------------------------

root = tk.Tk()
root.title("Tic-Tac-Toe AI")
root.geometry("420x500")

# Scoreboard
score_label = tk.Label(
    root,
    text="Player: 0    AI: 0    Draws: 0",
    font=("Arial", 16, "bold")
)

score_label.grid(row=0, column=0, columnspan=3, pady=15)

# Board Buttons
buttons = []

for i in range(9):

    btn = tk.Button(
        root,
        text="",
        font=("Arial", 28),
        width=5,
        height=2,
        command=lambda i=i: player_move(i)
    )

    btn.grid(row=(i // 3) + 1, column=i % 3)

    buttons.append(btn)

# Run Game
root.mainloop()