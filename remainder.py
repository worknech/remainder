import datetime
import time
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd

import pygame


def set():
    pass


root = Tk()
root.title('Напоминание')

label = Label(text='Установите напоминание')
label.pack(pady=10)

set_button = Button(text='Установить напоминание', command=set)
set_button.pack()

root.mainloop()