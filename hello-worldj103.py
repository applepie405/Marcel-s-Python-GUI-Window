from tkinter import *
from tkinter import ttk

# Create a window
root = Tk()
root.title("My GUI App")

# Create a frame for first 2 widgets
frame1 = ttk.Frame(root)
frame1.grid(row=0, column=0)
# Create a label and add it to the window using pack()
frame1 = ttk.Frame(root, text="My GUI App!")
frame1.grid(row=0, column=0, padx=10, pady=5)

#Create a StringVar() to store text
words = StringVar()

# Create a text entry field
frame1 = ttk.Frame(root, textvariable=words)
frame1.grid(row=1, column=0, padx=10, pady=5)

# Create a frame for the second 2 widgets
frame2 = ttk.Frame(root)
frame2.grid(row=1, column=0)
# Create a second label with longer text and add it to the window using pack()
label2 = ttk.Label(root, textvariable=words, wraplength=150)
label2.grid(row=2, column=0, padx=10, pady=5)

# Create a StringVar() for the chosen option
chosen_option = StringVar()

# Create a list of items for the Option Menu
options = ['Vanilla', 'Strawberry', 'Chocolate']

# Create the option menu and place in row 3, column 0
option_menu = ttk.OptionMenu(root, chosen_option, options[0], *options)
option_menu.grid(row=3, column=0, padx=10, pady=5)

# Run the main window loop
root.mainloop()
