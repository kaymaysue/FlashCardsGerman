import tkinter as tk
from tkinter import *
import random, csv

# ----------------------- Constants ----------------------------
current_word = None
# ----------------------- Functions ----------------------------

def pick_word():
    global current_word
    with open("data/german-words.csv") as data_file:
        data = list(csv.reader(data_file))
        current_word = random.choice(list(data))

def right_answer():
    # Move the list this word is in from data to words learned
    show_front_card()

def show_front_card():
    pick_word()
    canvas.itemconfig(card_image, image=FRONT_CARD)
    canvas.itemconfig(Card_title, text="German Word", fill="black")
    canvas.itemconfig(Card_word, text=current_word[0], fill="black")

    window.after(3000, show_back_card)

def show_back_card():
    canvas.itemconfig(card_image, image=BACK_CARD)
    canvas.itemconfig(Card_title, text="English", fill="white")
    canvas.itemconfig(Card_word, text=current_word[1], fill="white")


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
    bd=0,
    command=show_front_card
)
wrong_button.grid(row=1, column=0)

right_button = Button(
    window,
    image=CORRECT_IMG,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    bd=0,
    command=right_answer
)
right_button.grid(row=1, column=1)

# -------------------------- CARDS -----------------------------

pick_word()

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(
    window, 
    width=card_width, 
    height=card_height, 
    bg=BACKGROUND_COLOR, 
    highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_image = canvas.create_image(card_width//2, card_height/2, image=FRONT_CARD)

Card_title = canvas.create_text(
    card_width//2, 
    card_height//3, 
    text=" ", 
    font=("Ariel", 30, "italic")
)
Card_word = canvas.create_text(
    card_width//2, 
    card_height//2, 
    text=" ", 
    font=("Ariel", 50, "bold")
)

show_front_card()

window.mainloop()

# -------------------- testing ------------------------
