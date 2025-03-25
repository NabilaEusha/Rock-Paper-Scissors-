from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Function to resize images
def resize(path):
    return ImageTk.PhotoImage(Image.open(path).resize((120, 120), Image.LANCZOS))

#main window
window = Tk()
window.title("Rock Paper Scissor")
window.config(background="black")

# Load images
image_rock1 = resize("rock.jpg")
image_paper1 = resize("paper.png")
image_scissor1 = resize("scissor.png")
image_rock2 = resize("rock2.png")
image_paper2 = resize("paper2.jpeg")
image_scissor2 = resize("scissor2.jpg")

# Display images
label_computer = Label(window, image=image_scissor1)
label_player = Label(window, image=image_scissor2)
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)

# Score labels
computer_score = Label(window, text="0", font=("arial", 60, "bold"), bg="orange", fg="blue")
player_score = Label(window, text="0", font=("arial", 60, "bold"), bg="orange", fg="blue")
player_score.grid(row=1, column=3)
computer_score.grid(row=1, column=1)

# Indicators
player_indicator = Label(window, font=("arial", 40, "bold"), text="USER", bg="orange", fg="blue")
computer_indicator = Label(window, font=("arial", 40, "bold"), text="COMPUTER", bg="orange", fg="blue")
player_indicator.grid(row=0, column=4)
computer_indicator.grid(row=0, column=0)

# Variable to store selected round limit
round_limit = IntVar()
round_limit.set(5)  # Default round limit

# Update Message
def updateMessage(a):
    final_message['text'] = a

# Update Scores
def Computer_update():
    final = int(computer_score['text']) + 1
    computer_score["text"] = str(final)
    check_winner()

def Player_update():
    final = int(player_score['text']) + 1
    player_score["text"] = str(final)
    check_winner()

# Check for the winner based on chosen round limit
def check_winner():
    rounds = round_limit.get()
    if int(player_score["text"]) == rounds:
        updateMessage("You are the Champion! Well donee!!")
        disable_buttons()
    elif int(computer_score["text"]) == rounds:
        updateMessage("Computer is the Champion! he he he")
        disable_buttons()

# Disable buttons when the game is over
def disable_buttons():
    button_rock.config(state=DISABLED)
    button_paper.config(state=DISABLED)
    button_scissor.config(state=DISABLED)

# Reset game function
def reset_game():
    computer_score["text"] = "0"
    player_score["text"] = "0"
    final_message["text"] = ""
    label_computer.configure(image=image_scissor1)
    label_player.configure(image=image_scissor2)
    button_rock.config(state=NORMAL)
    button_paper.config(state=NORMAL)
    button_scissor.config(state=NORMAL)

# Game logic
to_select = ["rock", "paper", "scissor"]

def choice_update(a):
    choice_computer = to_select[randint(0, 2)]
    if choice_computer == "rock":
        label_computer.configure(image=image_rock1)
    elif choice_computer == "paper":
        label_computer.configure(image=image_paper1)
    else:
        label_computer.configure(image=image_scissor1)

    if a == "rock":
        label_player.configure(image=image_rock2)
    elif a == "paper":
        label_player.configure(image=image_paper2)
    else:
        label_player.configure(image=image_scissor2)

    winner_check(a, choice_computer)

def winner_check(p, c):
    if p == c:
        updateMessage("It's a tie!")
    elif p == "rock":
        if c == "paper":
            updateMessage("Computer Wins!!")
            Computer_update()
        else:
            updateMessage("You Win!!")
            Player_update()       
    elif p == "paper":
        if c == "scissor":
            updateMessage("Computer Wins!!")
            Computer_update()
        else:
            updateMessage("You Win!!")
            Player_update()       
    elif p == "scissor":
        if c == "rock":
            updateMessage("Computer Wins!!")
            Computer_update()
        else:
            updateMessage("You Win!!")
            Player_update()
    else:
        pass

# Final Message Display
final_message = Label(window, font=("arial", 30, "bold"), bg="black", fg="white")
final_message.grid(row=3, column=2)

# Buttons for Choices
button_rock = Button(window, width=10, height=2, text="ROCK", 
                     font=("arial", 20, "bold"), bg="white", fg="red", command=lambda: choice_update("rock"))
button_paper = Button(window, width=10, height=2, text="PAPER", 
                      font=("arial", 20, "bold"), bg="white", fg="red", command=lambda: choice_update("paper"))
button_scissor = Button(window, width=10, height=2, text="SCISSOR", 
                        font=("arial", 20, "bold"), bg="white", fg="red", command=lambda: choice_update("scissor"))

# Placing buttons
button_rock.grid(row=2, column=1)
button_paper.grid(row=2, column=2)
button_scissor.grid(row=2, column=3)

# Round Selection Option
Label(window, text="Choose Rounds:", font=("arial", 20, "bold"), bg="black", fg="white").grid(row=4, column=1)
round_entry = Spinbox(window, from_=1, to=20, textvariable=round_limit, font=("arial", 20, "bold"), width=5)
round_entry.grid(row=4, column=2)

# Reset Button
button_reset = Button(window, text="RESET", font=("arial", 20, "bold"), bg="red", fg="white", command=reset_game)
button_reset.grid(row=4, column=3)


window.mainloop()
