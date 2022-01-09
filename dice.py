
import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry('400x400')
root.title('D&D Roll the dice')

Blankline = tkinter.Label(root, text="")
Blankline.pack()

HeadingLabel = tkinter.Label(root, text="Hello from D&D World!",
    fg = "light green", 
        bg = "dark green",
        font = "Helvetica 16 bold italic")
HeadingLabel.pack()

dice = ['die1.png', 'die2.png', 'die3.png',
 'die4.png', 'die5.png', 'die6.png']
DiceImage = ImageTk.PhotoImage (Image.open (random.choice(dice)))

ImageLabel = tkinter.Label (root, image=DiceImage)
ImageLabel.image = DiceImage

ImageLabel.pack ( expand=True)

dice = ['die1.png', 'die2.png', 'die3.png',
 'die4.png', 'die5.png', 'die6.png']

DiceImage = ImageTk.PhotoImage (Image.open (random.choice(dice)))

ImageLabel = tkinter.Label (root, image=DiceImage)
ImageLabel.image = DiceImage

ImageLabel.pack ( expand=True)

def rolling_dice():
    DiceImage = ImageTk.PhotoImage (Image.open (random.choice(dice)))
    ImageLabel.configure(image= DiceImage)
    ImageLabel.image = DiceImage

button = tkinter.Button(root, text='Roll the Dice or Die', fg='blue', 
command=rolling_dice)
button.pack( expand=True)

root.mainloop()