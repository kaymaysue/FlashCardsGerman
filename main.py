import tkinter as tk
from tkinter import *
import random, pandas, csv

# ----------------------- Functions ----------------------------

def pick_word():
    with open("data/german-words.csv") as data_file:
        data = csv.reader(data_file)
        n = random.choice(list(data))
        return n


# -------------------------- UI -----------------------------

window = tk.Tk()
window.title("Flash Cards DE to EN")

BACKGROUND_COLOR = "#B1DDC6"
BACK_CARD = PhotoImage(file="images/card_back.png")
FRONT_CARD = PhotoImage(file="images/card_front.png")
CORRECT_IMG = PhotoImage(file="images/right.png")
INCORRECT_IMG = PhotoImage(file="images/wrong.png")

card_width = FRONT_CARD.width()
card_height = FRONT_CARD.height()

wrong_button = Button(
    window,
    image=INCORRECT_IMG,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    bd=0
)
wrong_button.grid(row=1, column=0)

right_button = Button(
    window,
    image=CORRECT_IMG,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    bd=0
)
right_button.grid(row=1, column=1)

# -------------------------- Front Card -----------------------------

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(
    window, 
    width=card_width, 
    height=card_height, 
    bg=BACKGROUND_COLOR, 
    highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

canvas.create_image(card_width//2, card_height/2, image=FRONT_CARD)

german_word = pick_word()

frontCard_title = canvas.create_text(
    card_width//2, 
    card_height//3, 
    text="German Word", 
    font=("Ariel", 30, "italic")
)
frontCard_word = canvas.create_text(
    card_width//2, 
    card_height//2, 
    text=german_word[0], 
    font=("Ariel", 50, "bold")
)

window.mainloop()

# -------------------- testing ------------------------
