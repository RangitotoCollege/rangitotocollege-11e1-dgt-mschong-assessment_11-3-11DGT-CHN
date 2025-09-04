from tkinter import *
m = Tk()
title = "Caio's Cool Collections"
m.title(title)
Game1 = "General Knowledge Quiz"
Game2 = "Wordle"
Game3 = "Hangman"

#Setting window size
width = 1080
height = 720
m.geometry("{}x{}".format(width, height))

#Frame
frame = Frame(m)
frame.pack(pady=20)

#Program Title
label = Label(frame, text=title, font=("Arial", 35))

#Prgram Menu
menu = Menu(m)
m.config(menu=menu)
help_menu = Menu(menu)
menu.add_cascade(label="Tutorial", menu=help_menu)
help_menu.add_command(label="How to play: {}".format(Game1))
help_menu.add_command(label="How to play: {}".format(Game2))
help_menu.add_command(label="How to play: {}".format(Game3))

button_width = 20
button_height = 5

#Menu Buttons
menu_button1 = Button(frame, text="Game 1", width=button_width, height=button_height)
menu_button2 = Button(frame, text="Game 2", width=button_width, height=button_height)
menu_button3 = Button(frame, text="Game 3", width=button_width, height=button_height)
menu_exit = Button(m, text="Exit Program", command=m.quit, width=button_width, height=round(button_height/2))

#program layout
label.grid(row=0, column=0, columnspan=3, sticky=W+E, pady=25)
menu_button1.grid(row=1, column=0)
menu_button2.grid(row=1, column=1, padx=40)
menu_button3.grid(row=1, column=2)
menu_exit.pack(fill=BOTH, side=BOTTOM, pady=20, padx=button_width*5)




m.mainloop()
