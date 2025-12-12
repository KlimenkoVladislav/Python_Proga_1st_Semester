# #1
# import tkinter as tk
# import random

# def nadpis():
#     res.config(text = random.choice(vibor))

# vibor = ['Ты сегодня сделаешь что-то крутое', 'Сегодня хороший день для чая', 'Твоя следующая оценка - 5']

# window = tk.Tk()
# window.geometry('500x500')
# knopka = tk.Button(window, text = 'Скажи мне что-нибудь', command = nadpis)
# knopka.pack()

# res = tk.Label(window, text = 'zadanie 1')
# res.pack()

# tk.mainloop()

# #2
# import tkinter as tk

# def for_red():
#     window.config(bg = 'red')
# def for_yellow():
#     window.config(bg = 'yellow')
# def for_green():
#     window.config(bg = 'green')

# window = tk.Tk()
# window.geometry('900x900')

# red_knopka = tk.Button(window, text = 'Красный', command=for_red)
# yellow_knopka = tk.Button(window, text = 'Жёлтый', command=for_yellow)
# green_knopka = tk.Button(window, text = 'Зелёный', command=for_green)
# red_knopka.pack()
# yellow_knopka.pack()
# green_knopka.pack()

# tk.mainloop()

# #3
# import tkinter as tk
# import random
# a = random.randint(1, 100)

# def res():
#     s = int(vvod.get())
#     if s==a:
#         otvet.configure(text = '«✅ Ты угадал!»')
#     if s<a:
#         otvet.configure(text = '«❌ Больше!»')
#     if s>a:
#         otvet.configure(text = '«❌ Меньше!»')

# window = tk.Tk()
# window.geometry('900x900')

# knopka = tk.Button(window, text = 'Угадать', command = res)
# knopka.pack()
# vvod = tk.Entry(window)
# vvod.pack()
# otvet = tk.Label(window, text = 'Подсказка программы')
# otvet.pack()

# tk.mainloop()

# #4
# import tkinter as tk

# def terpenie():
#     global kol
#     kol+=1
#     if kol==7:
#         metka = tk.Label(window, text = '«Ты настойчив! Вот тебе сюрприз: ты победил!»')
#         metka.pack()

# kol = 0
# window = tk.Tk()
# window.geometry('900x900')

# knopka = tk.Button(window, text = 'Запустить', command=terpenie)
# knopka.pack()

# tk.mainloop()

#5
import tkinter as tk
import random

def for_1():
    global a
    if a==1:
        knopka_1.configure(text='«Поздравляем! Ты нашёл секрет!»')
    else:
        knopka_1.configure(text='«Попробуй ещё!»')
def for_2():
    global a
    if a==2:
        knopka_2.configure(text='«Поздравляем! Ты нашёл секрет!»')
    else:
        knopka_2.configure(text='«Попробуй ещё!»')
def for_3():
    global a
    if a==3:
        knopka_3.configure(text='«Поздравляем! Ты нашёл секрет!»')
    else:
        knopka_3.configure(text='«Попробуй ещё!»')
def for_4():
    global a
    if a==4:
        knopka_4.configure(text='«Поздравляем! Ты нашёл секрет!»')
    else:
        knopka_4.configure(text='«Попробуй ещё!»')

a = random.randint(1, 4)

window = tk.Tk()
window.geometry('900x900')

knopka_1 = tk.Button(window, text = '1', command=for_1, font=('Arial', 40))
knopka_2 = tk.Button(window, text = '2', command=for_2, font=('Arial', 40))
knopka_3 = tk.Button(window, text = '3', command=for_3, font=('Arial', 40))
knopka_4 = tk.Button(window, text = '4', command=for_4, font=('Arial', 40))
knopka_1.pack()
knopka_2.pack()
knopka_3.pack()
knopka_4.pack()

tk.mainloop()