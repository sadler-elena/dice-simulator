from tkinter import *
from random import *



#Initiating the window!
window = Tk()

#Putting title!
window.title("Dice Simulator")

#Description
description = Label(window, text='Welcome to the Dice Simulator! Press roll to generate a number between 1 and 6!')
description.grid(column=1, row=0)

#Defining roll function.
def roll():
    #Make it show all dice variations
    randomNumber = randint(1, 6)
    numberDisplay = Label(window, text=randomNumber)
    numberDisplay.grid(column=1, row=3)

rollButton = Button(window, text="Roll", bg='red', fg='white', command=roll)
rollButton.grid(column=1, row=4)

exitButton = Button(window, text='Exit', command=window.quit)
exitButton.grid(column=1, row=6)



window.mainloop()





