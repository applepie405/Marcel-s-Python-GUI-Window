from tkinter import *
from tkinter import ttk

# Create a window
root = Tk()
root.title("My GUI App")

# Create a label and add it to the window using pack()
label1 = ttk.Label(root, text="My GUI App!")
label1.grid(row=0, column=0, padx=10, pady=5)

#Create a StringVar() to store text
words = StringVar()

# Create a text entry field
words_entry = ttk.Entry(root, textvariable=words)
words_entry.grid(row=1, column=0, padx=10, pady=5)

# Create a second label with longer text and add it to the window using pack()
label2 = ttk.Label(root, textvariable=words, wraplength=150)
label2.grid(row=2, column=0, padx=10, pady=5)

# Create a StringVar() for the chosen option
chosen_option = StringVar()
chosen_option.set
# Create a list of items for the Option Menu
options = ['flavors', 'cars', 'movies', 'narcissm']

# Create the option menu and place in row 3, column 0
option_menu = ttk.OptionMenu(root, *options)
option_menu.grid(row=3, column=0, padx=10, pady=5)

# Run the main window loop
root.mainloop()
