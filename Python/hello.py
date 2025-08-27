import tkinter
m = tkinter.Tk()
title = "Caio's Cool Collections"
m.title(title)
width = 1080
height = 720
half_width = width / 2
half_height = height / 2
m.geometry("{}x{}".format(width, height))
m.resizable(False, False) # Learned this code from stack overflow
label = tkinter.Label(m, text=title, font=("Arial", 30), justify="left").grid(row=0, column=0, columnspan=3, pady=40, padx= half_width-200)

m.button = tkinter.Button(m, text="Close", command=m.destroy).grid(row=1, column=1,)
m.mainloop()
