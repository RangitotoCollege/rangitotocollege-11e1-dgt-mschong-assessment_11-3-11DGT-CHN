from tkinter import *
m = Tk()

global title, Game1, Game2, Game3
title = "Caio's Cool Collections"
m.title(title)
Game1 = "General Knowledge Quiz"
Game2 = "Wordle"
Game3 = "Hangman"

#Setting window size
width = 1080
height = 720
m.geometry("{}x{}".format(width, height))

#Button size
global button_width, button_height
button_width = 20
button_height = 5

#Initial Frame
global frame
frame = Frame(m)
frame.pack(pady=20)

#Tutorial Functions
def GK_tutorial():
    tutorial_window = Toplevel(m)
    tutorial_window.resizable(False, False) # code learned from stack overflow
    tutorial_window.title("How to play: {}".format(Game1))
    tutorial_label = Label(tutorial_window, text="How to play: General Knowledge Quiz", font=("Arial", 16, "bold"))
    tutorial_label.pack(pady=10)
    tutorial_desc = Label(tutorial_window, text="This game is simple! You will be asked 10 randomly selected questions,\n"
    "and all you have to do is answer them correctly and you can get all the\n"
    "points!\n\nGood Luck!", font=("Arial", 12), justify=LEFT)
    tutorial_desc.pack(padx=20, pady=20)
    ok_button = Button(tutorial_window, text="OK", width=round(button_width/4), command=tutorial_window.destroy)
    ok_button.pack(pady=10)

def W_tutorial():
    tutorial_window = Toplevel(m)
    tutorial_window.resizable(False, False) # code learned from stack overflow
    tutorial_window.title("How to play: {}".format(Game2))
    tutorial_label = Label(tutorial_window, text="How to play: Wordle", font=("Arial", 16, "bold"))
    tutorial_label.pack(pady=10)
    tutorial_desc = Label(tutorial_window, text="I'm sure you know how this goes, you will be given 6 chances to guess a 5 letter word.\n"
    "After each guess, the letters will change colour to show how close you are\n"
    "to guessing the word. green means the letter is in the correct position,\n"
    "yellow means the letter is in the word but in the wrong position,\n"
    "and grey means the letter is not in the word at all.\n\nGood Luck!", font=("Arial", 12), justify=LEFT)
    tutorial_desc.pack(padx=20, pady=20)
    ok_button = Button(tutorial_window, text="OK", width=round(button_width/4), command=tutorial_window.destroy)
    ok_button.pack(pady=10)

def HM_tutorial():
    tutorial_window = Toplevel(m)
    tutorial_window.resizable(False, False) # code learned from stack overflow
    tutorial_window.title("How to play: {}".format(Game3))
    tutorial_label = Label(tutorial_window, text="Welcome to Hangman!", font=("Arial", 16, "bold"))
    tutorial_label.pack(pady=10)
    tutorial_desc = Label(tutorial_window, text="In this game, you will be given a word with missing letters.\n"
    "You have to guess the word by suggesting letters within a certain number of guesses.\n"
    "For each incorrect guess, a part of the hangman will be drawn.\n"
    "You have 6 incorrect guesses before the hangman is fully drawn and you lose!\n\nGood Luck!", font=("Arial", 12), justify=LEFT)
    tutorial_desc.pack(padx=20, pady=20)
    ok_button = Button(tutorial_window, text="OK", width=round(button_width/4), command=tutorial_window.destroy)
    ok_button.pack(pady=10)

#Game Functions
def GK_game():
    menu_frame.destroy()

    q_a = {
        "What is the closest planet to the sun?": "Mercury",
        "Who came up with the term 'debugbing'?": "Grace Hopper",
        "What program was ChatGPT created on?": "Python",
        "What is the meaning of life, the universe and everything?": "42",
        "What does the acronym 'www' stand for?": "World Wide Web",
        "What is the name of the first 3D platforming video game?": "Super Mario 64",
    }

    global GK_frame
    GK_frame = Frame(m)
    GK_frame.pack(pady=20)

    GK_label = Label(GK_frame, text="General Knowledge Quiz", font=("Arial", 30))
    GK_label.grid(row=0, column=0, columnspan=2, sticky=W+E)
    global menu_exit
    menu_exit.config(text="Exit to Menu", command=exit_to_menu)



def exit_to_menu():
    GK_frame.destroy()
    menu_exit.destroy()
    open_menu()

#Prgram Menu
def tutorial_menu():
    menu = Menu(m)
    m.config(menu=menu)
    help_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Tutorial", menu=help_menu)
    help_menu.add_command(label="How to play: {}".format(Game1), command=GK_tutorial)
    help_menu.add_command(label="How to play: {}".format(Game2), command=W_tutorial)
    help_menu.add_command(label="How to play: {}".format(Game3), command=HM_tutorial)

#Open Menu function
def open_menu():
    tutorial_menu()
        
    frame.destroy()
    global menu_frame
    menu_frame = Frame(m)
    menu_frame.pack(pady=20)

    #Program Title
    if "Caio" in player_name.title():
        text = "Welcome, Creator!"
    elif "Chong" in player_name.title():
        text = "Welcome, miss!"
    elif "Ethan" in player_name.title():
        text = "Get out of my program, Ethan."
    else:
        text = "Welcome, {}!".format(player_name)
    welcome_label = Label(menu_frame, text=text, font=("Arial", 18))
    label = Label(menu_frame, text="Caio's Cool Collections", font=("Arial", 35))

    #Menu Buttons
    menu_button1 = Button(menu_frame, text="Game 1", width=button_width, height=button_height, command=GK_game)
    menu_button2 = Button(menu_frame, text="Game 2", width=button_width, height=button_height)
    menu_button3 = Button(menu_frame, text="Game 3", width=button_width, height=button_height)
    global menu_exit
    menu_exit = Button(m, text="Exit Program", command=m.quit, width=button_width, height=round(button_height/2))

    #program layout
    welcome_label.grid(row=0, column=0, columnspan=3, sticky=W+E)
    label.grid(row=1, column=0, columnspan=3, sticky=W+E, pady=20)
    menu_button1.grid(row=2, column=0, pady=30)
    menu_button2.grid(row=2, column=1, padx=40)
    menu_button3.grid(row=2, column=2)
    menu_exit.pack(fill=BOTH, side=BOTTOM, pady=20, padx=button_width*5)


#Menu function
def menu():
    global player_name, name_entry
    player_name = name_entry.get()
    
    if name_entry.get() == "":
        global error_mes
        error_mes.destroy()
        error_mes = Label(frame, text="Please enter a name to continue.", font=("Arial", 12), fg="red")
        error_mes.pack()
    else:
        open_menu()

#Beginning message
title = Label(frame, text="Welcome to Caio's Cool Collections!", font=("Arial", 30), justify=CENTER)
subtext = Label(frame, text="Before we begin, please enter your name below:", font=("Arial", 18), justify=CENTER)
title.pack(pady=(50,20))
subtext.pack(pady=(20,50))
global name_entry
name_entry = Entry(frame, font=("Arial", 16))
enter_button = Button(frame, text="Enter", font=("Arial", 12), command=menu)
error_mes = Label(frame, text="", font=("Arial", 12), fg="red")
error_mes.pack()
name_entry.pack()
enter_button.pack(pady=20)

m.mainloop()
