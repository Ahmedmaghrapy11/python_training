from tkinter import *
from tkinter import ttk

root = Tk()

button1 = ttk.Button(root, text="click me 1")
button1.pack()
button2 = ttk.Button(root, text="click me 2")
button2.pack()
button3 = ttk.Button(root, text="click me 3")
button3.pack()

def buttonFunction(x):
    print(f"clicked {x} !")

button1.config(command= lambda : buttonFunction(1))
button2.config(command= lambda : buttonFunction(2))
button3.config(command= lambda : buttonFunction(3))

root.mainloop()