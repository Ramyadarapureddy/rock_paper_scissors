#Importing Libraries
from tkinter import *
import random

# Initializing Global variables

player_score = 0
computer_score = 0
options = [('rock',0),('paper',1),('scissors',2)]

# Defining the Player Choice Function
def player_choice(player_input):
    global player_score, computer_score
    computer_input = get_computer_choice()
    player_choice_label.config(text="You Selected : " +player_input[0])
    computer_choice_label.config(text="Computer Selected : " +computer_input[0])
    
    if (player_input == computer_input):
        winner_label.config(text= "Tie😑" )

    elif ((player_input[1] - computer_input[1])%3 == 1):
        player_score += 1
        winner_label.config(text= "You Won🥳")
        player_score_label.config(text= "Your Score : " +str(player_score))    
    else:
        computer_score += 1
        winner_label.config(text= "You Lost 😕")
        computer_score_label.config(text= "Computer Score : " +str(computer_score))


# Defining the computer choice function  
def get_computer_choice():
    return random.choice(options)

# Creating the main Window
game_window = Tk()
game_window.title("ROCK🪨-PAPER📃-SCISSOR✂️")
game_window.minsize(850,550)


# Setting Up Fonts and Labels

game_title = Label(text="ROCK PAPER SCISSOR", font=("Segoe UI Black",30,"bold"), fg='purple', pady=10)
game_title.pack()

winner_label = Label(text="Let's Start the Game...", fg="#CC0066", font=('Times New Roman',20, "bold"),pady=10)
winner_label.pack()

#Creating Input Frame and Player Options
input_frame = Frame(game_window, pady=20)
input_frame.pack()

rock_btn = Button(input_frame,text='Rock',font=('Segoe UI Black',15, 'bold'), width=10,height=3, bd=2, bg="#00cc66",fg="white",activebackground="#3399ff",activeforeground="white", command= lambda:player_choice(options[0]) )
rock_btn.grid(row= 1, column=1,padx=15, pady=8)

paper_btn = Button(input_frame,text='Paper',font=('Segoe UI Black',15, 'bold'), width=10,height=3, bd=2, bg="#00cc66",fg="white",activebackground="#ff007f",activeforeground="white", command= lambda:player_choice(options[1]) )
paper_btn.grid(row= 1, column=2,padx=15, pady=8)

scissor_btn = Button(input_frame,text='Scissor',font=('Segoe UI Black',15, 'bold'), width=10,height=3, bd=2, bg="#00cc66",fg="white",activebackground="#cc6600",activeforeground="white", command= lambda:player_choice(options[2]) )
scissor_btn.grid(row= 1, column=3,padx=20, pady=8)

# Displaying Scores and Choices
score_label = Label(input_frame, text="Scores : ", font=('Segoe UI Black',15,"bold"), fg="purple")
score_label.grid(row=2,column=2,pady=30)

player_choice_label = Label(input_frame, text="You Selected :-- ", font=('Times New Roman',15,"bold"), fg="#3333ff")
player_choice_label.grid(row=3,column=1,pady=5)

player_score_label = Label(input_frame, text="Your Score :-- ", font=('Times New Roman',15,"bold"), fg="#3333ff")
player_score_label.grid(row=3,column=3,padx=10 ,pady=5)

computer_choice_label = Label(input_frame, text="Computer Selected :-- ", font=('Times New Roman',15,"bold"), fg="#3333ff")
computer_choice_label.grid(row=4,column=1,pady=5)

computer_score_label = Label(input_frame, text="Computer Score :-- ", font=('Times New Roman',15,"bold"), fg="#3333ff")
computer_score_label.grid(row=4,column=3,padx=10, pady=5)


game_window.mainloop()