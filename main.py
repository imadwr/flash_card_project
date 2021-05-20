from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------- read data file --------------- #
data = pandas.read_csv("./data/french_words.csv")
data_dict = pandas.DataFrame.to_dict(data)
print(data_dict)
french_words_dict = data_dict["French"]
english_words_dict = data_dict["English"]

data_list = []

for index in french_words_dict:
    french_word = french_words_dict[index]
    english_word = english_words_dict[index]
    new_dict = {
        french_word: english_word
    }
    data_list.append(new_dict)


def generate_word():
    random_dict = random.choice(data_list)
    for fr_word in random_dict:
        canvas.itemconfig(title, text="French")
        canvas.itemconfig(word, text=fr_word)



# --------------------- UI --------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="Title", font=("Arial", 30, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 50, "bold"))
generate_word()
canvas.grid(row=0, column=0, columnspan=2)

# buttons

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=generate_word)
right_button.grid(row=1, column=1)






window.mainloop()

