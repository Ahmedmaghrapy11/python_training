from tkinter import *
from tkinter import ttk

# build the main frame of the UI
root = Tk()

# entry field for the user
entry1 = ttk.Entry(root, width=40)
entry1.pack()

# button to get the text entered by the user
button1 = ttk.Button(root, text="Get Text")
button1.pack()

# # put an image with the button
# login = PhotoImage(file = "pexels-drift-shutterbug-2085998.jpg")
# resize_login = login.subsample(10,10)       # resize the image

# stupid function
def buttonClicked():
    print(entry1.get())
    entry1.delete(0, END)

# link the stupid function with the button
button1.config(command=buttonClicked)

# make the root appear in the windows
root.mainloop()