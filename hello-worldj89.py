from ktinker import *

root = Tk()
root.title("Goal Tracker")

#Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can deposit or withdraw money and see your progress towards your goals.")

#Create and pack the message label
message_label = Label(root, textvariable=message_text, wraplength=250)
message_label.pack()

#Create the PhotoImage and label to hold it
neutral_image = Photoimage(file="/images/python/neutral.png")
image_label = Label(root, image=neutral_image)
image_label.pack()

#Create and set the accountdetails variable
account_details = StringVar()
account_details.set("Savings: $500 - 25% 0f $2000 goal \nTotal balance: $500")

#Create the details label and pack it into the GUI
details_label = label(root, textvariable=account_details)   
details_label.pack()

#Run the mainloop
root.mainloop()
