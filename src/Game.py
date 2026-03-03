import tkinter as tk
import random

def play(user_input):
    dict1 = {"s": 1, "g": 0, "w": -1}
    dict2 = {1: "Snake", 0: "Gun", -1: "Water"}

    computer = random.choice([-1, 0, 1])
    you = dict1[user_input]

    comp_choice = dict2[computer]
    user_choice = dict2[you]

    # Determine result
    if computer == you:
        result = "It's a draw."
    elif (computer == 1 and you == 0) or \
         (computer == -1 and you == 1) or \
         (computer == 0 and you == -1):
        result = "You win!!"
    elif (computer == 1 and you == -1) or \
         (computer == -1 and you == 0) or \
         (computer == 0 and you == 1):
        result = "You lose!!"
    else:
        result = "Something went wrong..."

    result_text.set(f"Computer chose: {comp_choice}\nYou chose: {user_choice}\n\n{result}")

# GUI Setup
window = tk.Tk()
window.title("Snake, Water & Gun Game")
window.geometry("400x300")

title = tk.Label(window, text="Snake, Water & Gun Game", font=("Helvetica", 16))
title.pack(pady=10)

btn_frame = tk.Frame(window)
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Snake", width=10, font=("Helvetica", 12), command=lambda: play("s")).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Water", width=10, font=("Helvetica", 12), command=lambda: play("w")).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Gun", width=10, font=("Helvetica", 12), command=lambda: play("g")).grid(row=0, column=2, padx=10)

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, font=("Helvetica", 12), justify="center")
result_label.pack(pady=20)

window.mainloop()
