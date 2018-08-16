from tkinter import *
from random import *
from PIL import Image, ImageTk


#Initiating the window!
window = Tk()

#Putting title!
window.title("Dice Simulator")

#Description
description = Label(window, text='Welcome to the Dice Simulator! Press roll to generate a number between 1 and 6!')
description.grid(column=1, row=0)

#Defining roll function.
def showImg(file):
    global load
    load = Image.open(file)
    global render
    render = ImageTk.PhotoImage(load)
    diceImg = Label(window, image=render)
    diceImg.grid(column=1, row=7)

def roll():
    randomNumber = randint(1, 6)
    file_name = str(randomNumber) + '.png'
    showImg(file_name)



rollButton = Button(window, text="Roll", bg='red', fg='white', command=roll)
rollButton.grid(column=1, row=4)

exitButton = Button(window, text='Exit', command=window.quit)
exitButton.grid(column=1, row=6)


window.mainloop()





