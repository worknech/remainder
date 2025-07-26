import datetime
import time
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd

import pygame

# Глобальные переменные
t = 0  # Хранит временную метку (timestamp) для напоминания
music = False  # Флаг, указывающий, играет ли музыка в данный момент


def set_t():
    """Функция для установки времени и текста напоминания"""
    global t
    rem = sd.askstring('Время напоминания', 'Введите время напоминания в формате ЧЧ:ММ (в 24 часовом формате)')
    try:
        # Проверка формата времени
        if ':' not in rem or len(rem.split(':')) != 2:
            mb.showerror('Ошибка', 'Используйте формат ЧЧ:ММ')

        # Разделяем часы и минуты и преобразуем в числа
        hour, minute = map(int, rem.split(':'))

        # Проверка допустимости значений времени
        if not (0 <= hour < 24 and 0 <= minute < 60):
            mb.showerror('Ошибка', "Время должно быть в пределах 00:00-23:59")

        # Получаем текущее время
        now = datetime.datetime.now()

        # Создаем объект datetime с указанным временем на сегодня
        dt = now.replace(hour=hour, minute=minute, second=0)

        # Преобразуем в timestamp (количество секунд с 1970-01-01)
        t = dt.timestamp()

        # Запрашиваем текст напоминания
        text = sd.askstring('Текст напоминания', 'Введите текст напоминания')

        # Обновляем текст на экране
        label.config(text=f'Напоминание на {hour:02}:{minute:02} с текстом "{text}"')

    except ValueError as ve:
        mb.showerror('Ошибка ввода', str(ve))
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
    """Функция проверки, не наступило ли время напоминания"""
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load('remainder.mp3')
    pygame.mixer.music.play()


def stop_music():
    """Функция остановки воспроизведения звука"""
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    label.config(text='Установить новое напоминание')


# Создание главного окна приложения
root = Tk()
root.title('Напоминание')

# Создаем текстовую метку
label = Label(text='Установите напоминание', font=('Arial', 14))
label.pack(pady=10)

# Создаем кнопку для установки напоминания
set_button = Button(text='Установить напоминание', command=set_t)
set_button.pack(pady=10)

# Создаем кнопку для остановки музыки
stop_button = Button(text='Остановить музыку', command=stop_music)
stop_button.pack(pady=10)

check()
root.mainloop()
