
from tkinter import *
from PIL import Image, ImageTk
from numpy import right_shift, size
from translate import Translator


root = Tk()
root.title("Matheus Brandão - Tradutor")
root.config(bg='Ghost White')
root.geometry('500x280')
root.minsize(500,280)
root.maxsize(500,280)

InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()

LanguageChoices = {'Chinese', 'English','French','German','Hindi', 'Portuguese', 'Russian', 'Spanish'}
InputLanguageChoice.set('English')
TranslateLanguageChoice.set('Portuguese')

InputLanguageChoiceMenu=OptionMenu(root,InputLanguageChoice,*LanguageChoices)
Label(root,text="Escolha um idioma para traduzir", font="arial 16 bold", bg= 'Ghost White').pack(pady=10,padx=0)
InputLanguageChoiceMenu.place(x=100,y=70, width=100,height=30)

NewLanguageChoiceMenu=OptionMenu(root,TranslateLanguageChoice,*LanguageChoices)
Label(root, text='para', font="arial 14 bold", bg= 'Ghost White').pack(pady=20,padx=50)
NewLanguageChoiceMenu.place(x=300,y=70, width=100,height=30)

Label(root,text="Digite o texto:", font="arial 12 bold", bg= 'Ghost White', fg='Red').place(y=110, x=30)
TextVar = StringVar()
entry_field = Entry(root, textvariable=TextVar)
entry_field.place(x=30,y=140,width=180,height=110)


Label(root,text="Tradução:", font="arial 12 bold", bg= 'Ghost White', fg='Red').place(y=110, x=285)
OutputVar = StringVar()
entry_field = Entry(root, textvariable=OutputVar).place(x=288,y=140,width=180,height=110)


def Translate():
    translator = Translator(from_lang=InputLanguageChoice.get(), to_lang=TranslateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)

Button(root, text="Traduzir",command=Translate, relief=GROOVE).place(y=180, x=220)   
    
def Exit():
    root.destroy()

Button(root, text="Exit",command=Exit, relief=GROOVE).place(y=210, x=230)  
        
root.mainloop()