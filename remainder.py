import datetime
import time
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd

import pygame

t = 0


def set_t():
    global t
    rem = sd.askstring('Время напоминания', 'Введите время напоминания ыв формате ЧЧ:ММ (в 24 часовом формате)')
    try:
        hour = int(rem.split(':')[0])
        minute = int(rem.split(':')[1])
        now = datetime.datetime.now()
        print(now)
        dt = now.replace(hour=hour, minute=minute, second=0)
        print(dt)
        t = dt.timestamp()
        print(t)
    except Exception as e:
        mb.showerror('Ошибка!', f'Произошла ошибка {e}')


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = 0
    root.after(10000, check)


def play_snd():
    pygame.mixer.init()
    pygame.mixer.music.load('remainder.mp3')
    pygame.mixer.music.play()


root = Tk()
root.title('Напоминание')

label = Label(text='Установите напоминание', font=('Arial', 14))
label.pack(pady=10)

set_button = Button(text='Установить напоминание', command=set_t)
set_button.pack()

check()
root.mainloop()
