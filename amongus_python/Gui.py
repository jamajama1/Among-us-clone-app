import amongUs
from tkinter import *

root = Tk()
root.title('Version 1.0')
root.geometry("695x530")
w = 695
h = 530
#Background for gui
root.configure(bg="black")

#Label containing game title
gameTitle = Label(root, text="AMONG US", fg="red", bg="black")
gameTitle.config(font=("Phosphate", 44))
gameTitle.place(relx=0.5, rely=0.5, anchor='center')

#Online button
online = Button(root, text="Online", command= amongUs.Game(695, 530).run()) #online button will automatically run game code
howTo = Button(root, text="How To Play")

online.pack()
howTo.pack()

root.mainloop()

