from tkinter import *

#create a window
root = Tk()
root.title("My GUI App")

#create a label and add it to the window using pack()
label1 = Label(root, text="My GUI App")
label1.pack()

#create a StringVar() to store text
words = StringVar()

#create a text entry field
words-entry = Entry(root, textvariable=words, bg="limegreen", fg="yellow", selectbackground="black", selectforeground="blue")
wo0rds_entry.pack()

# Create a second label with longer text and add it to the window using pack()
label2 = Label(root, textvariable=words, wraplength=150)
label2.pack()

# Run the main window loop
root.mainloop()

