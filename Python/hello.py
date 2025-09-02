from tkinter import *
m = Tk()
title = "Caio's Cool Collections"
m.title(title)

#Setting window size and boundaries
width = 1080
height = 720
m.geometry("{}x{}".format(width, height))

#Frame
frame = Frame(m)
frame.pack(pady=20)

#Program Title
label = Label(frame, text=title, font=("Arial", 30))

help = Button(frame, text="Help")
menu_button1 = Button(frame, text="Game 1")
menu_button2 = Button(frame, text="Game 2")
menu_button3 = Button(frame, text="Game 3")



label.grid(row=0, column=0, columnspan=3, sticky=W+E, pady=20)
menu_button1.grid(row=1, column=0)
menu_button2.grid(row=1, column=1)
menu_button3.grid(row=1, column=2)




m.mainloop()
