from tkinter import *

# Create a window
root = Tk()
root.title("Goal Tracker")

# Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can deposit or withdraw money and see your progress towards your goals.")

# Create the message label and add it to the window using pack()

message_label = Label(root, wraplength=250, textvariable=message_text)
message_label.pack()
# Run the main window loop
root.mainloop()
