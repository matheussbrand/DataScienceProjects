from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer) :
    while True :
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H-%M-%S")
        date = current_time.strftime("%D/%M/%Y")
        print("Data definida:", date)
        print(now)
        if now == set_alarm_timer:
            print("Hora de acordar!")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break

def actual_time() :
    set_alarm_timer = f"{hour.get() } : {min.get () } : {sec.get() }"
    alarm(set_alarm_timer)

clock = Tk()

clock.title("Relógio do Matheus")
clock.geometry("400x200")
time_format=Label(clock, text= "Insira a hora no formato 24 horas!", fg="red",bg="black",font="Arial") .place(x=60,y=120)
addTime = Label (clock, text= "Hora   Min   Sec",font=60) .place(x = 110)
setYourAlarm = Label (clock, text = "Quando acordar",fg="blue",relief="solid",font=("Helevetica",7,"bold")) .place(x=0, y=29)

hour = StringVar ()
min = StringVar ()
sec = StringVar ()

hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15) .place(x=110, y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15) .place(x=150, y=30)
secTime= Entry(clock,textvariable = sec,bg = "pink",width = 15) .place(x=200, y=30)

submit = Button(clock, text = "Programar Alarme",fg="red",width = 10, command = actual_time) .place(x =110, y =70)
clock.mainloop()
