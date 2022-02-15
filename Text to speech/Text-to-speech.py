from importlib.metadata import entry_points
from tkinter import *
from gtts import gTTS
from playsound import playsound
import os


root = Tk()
root.geometry("360x350")
root.configure(bg='ghost white')
root.title("Matheus Brandão -  Text to Speech")

Label(root, text ="Escreva aqui", font = "arial 20 bold", bg='white smoke') .pack()
Label(text ="Matheus Brandão (matheussbrand@gmail.com)", font='arial 10 bold', bg='white smoke', width = '60') .pack(side = 'bottom')

Msg = StringVar()
Label(root, text="Insira o texto", font = 'arial 15 bold', bg ='white smoke') .place(x=120,y=60)
entry_field = Entry(root, textvariable = Msg, width ='50')
entry_field.place(x=30,y=100)

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save(f'{Message}.mp3')
    playsound(f'{Message}.mp3')
    os.remove(f'{Message}.mp3')
    
def Exit():
    root.destroy()

def Reset():
    Msg.set("")



Button(root, text = "Play", font ='arial 15 bold', command = Text_to_speech ,width='4').place(x=80,y=140)     
Button(root, font = 'arial 15 bold', text = 'Exit', width = '4', command = Exit, bg = 'OrangeRed1').place(x=235, y=140)
Button(root, font = 'arial 15 bold',text = 'Reset', width = '6', command = Reset) .place(x=140,y=190)

root.mainloop ()