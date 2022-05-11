from tkinter import *
from tkinter import ttk

root = Tk()

def key_press(event):
    print(f"type of event is {event.type}")
    print("ctrl + c")

root.bind('<Control-c>', key_press)

def button_press(event):
    print("button is pressed!")

button = ttk.Button(root, text = "click")
button.pack()
button.bind("<ButtonPress>", button_press)

root.mainloop()