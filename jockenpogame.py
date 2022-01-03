from tkinter import *
import random

root = Tk ()
root.geometry('400x400')
root.resizable(0,0)
root.title('Pedra, Papel e Tesoura - Jockenpo')
root.config(bg ='seashell3')

Label (root, text = 'Pedra, Papel e Tesoura' , font='arial 20 bold', bg = 'seashell2') .pack()

user_take = StringVar ()
Label (root, text = 'escolha um: pedra, papel, tesoura' , font='arial 15 bold', bg = 'seashell2') .place(x = 20,y=70)
Entry(root, font = 'arial 15', textvariable = user_take, bg = 'antiquewhite2').place(x=90,y=130)

comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'pedra'
elif comp_pick == 2:
    comp_pick = 'papel'
else:
    comp_pick == 'scissors'

Result = StringVar ()

def play ():
    user_pick = user_take.get ()
    if user_pick == comp_pick:
        Result.set('empate, vocês dois selecionam o mesmo')
    elif user_pick == 'pedra' and comp_pick == 'papel':
        Result.set('você perdeu, o computador escolheu paper')
    elif user_pick == 'pedra' and comp_pick == 'tesoura':
        Result.set('você ganhou, o computador escolheu tesoura')
    elif user_pick == 'papel' and comp_pick == 'tesoura':
        Result.set('você perdeu, o computador escolheu tesoura')
    elif user_pick == 'papel' and comp_pick == 'pedra':
        Result.set('você ganhou, o computador escolheu pedra')
    elif user_pick == 'tesoura' and comp_pick == 'pedra':
        Result.set('você perdeu, o computador escolheu pedra')
    elif user_pick == 'tesoura' and comp_pick == 'papel':
        Result.set('você ganhou, o computador escolheu papel')
    else:
        Result.set('invalido: escolha um - pedra, papel ou tesoura')

def Reset ():
    Result.set("")
    user_take.set("")

def Exit ():
    root.destroy()

Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', text = 'COMEÇAR'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310)

Button(root, font = 'arial 13 bold', text = 'SAIR'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)


root.mainloop()
