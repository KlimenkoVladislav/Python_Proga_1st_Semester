# #1
# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.title("Список покупок")
# root.geometry("400x400")

# # Listbox
# listbox = tk.Listbox(root, selectmode=tk.SINGLE)
# listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# # Поле ввода
# entry = tk.Entry(root, width=40)
# entry.pack(pady=5)

# def add_item():
#     item = entry.get().strip()
#     if item:
#         listbox.insert(tk.END, item)
#         entry.delete(0, tk.END)
#     else:
#         messagebox.showwarning("Ошибка", "Ничего не написано")      #добавил обработку пустого ввода

# def delete_item():
#     sel = listbox.curselection()
#     if sel:
#         listbox.delete(sel[0])
#         messagebox.showinfo("Удалено", "Элемент удалён")
#     else:
#         messagebox.showwarning("Ошибка", "Ничего не выбрано")

# def edit_item():
#     selected = listbox.curselection()
#     if not selected:
#         messagebox.showwarning("Ошибка", "Выберите элемент")
#         return

#     index = selected[0]

#     edit_win = tk.Toplevel(root)
#     edit_win.title("Редактировать")
#     edit_win.geometry("250x100")
#     edit_win.grab_set()

#     edit_entry = tk.Entry(edit_win, width=30)
#     edit_entry.pack(pady=10)
#     edit_entry.focus_set()

#     def save():
#         new_text = edit_entry.get().strip()
#         if new_text:
#             listbox.delete(index)
#             listbox.insert(index, new_text)
#             edit_win.destroy()
#         else:
#             messagebox.showwarning("Ошибка", "Ничего не написано")      #добавил обработку пустого ввода

#     tk.Button(edit_win, text="Сохранить", command=save).pack(pady=10)

# # === КНОПКИ ===
# tk.Button(root, text="Добавить", command=add_item).pack(pady=2)
# tk.Button(root, text="Удалить", command=delete_item).pack(pady=2)
# tk.Button(root, text="Редактировать", command=edit_item).pack(pady=2)

# # Добавим немного данных
# for item in ["Хлеб", "Молоко", "Яйца"]:
#     listbox.insert(tk.END, item)

# root.mainloop()


# #2
# import tkinter as tk
# import tkinter.messagebox as msg 

# window = tk.Tk()
# window.geometry("400x450")
# window.title("Телефонная книга")

# label_name = tk.Label(window, text="Имя:")
# label_name.pack(pady=5)
# name = tk.Entry(window, width=30)
# name.pack(pady=5)

# label_phone = tk.Label(window, text="Телефон:")
# label_phone.pack(pady=5)
# phone = tk.Entry(window, width=30)
# phone.pack(pady=5)

# kniga = tk.Listbox(window, width=40, height=15, selectmode='multiple')
# kniga.pack(pady=10)

# def f_dobavit():
#     a = name.get()
#     b = phone.get()
#     if not a or not b:
#         msg.showerror('error', 'заполните оба поля')
#     else:
#         kniga.insert(tk.END, a+' - '+b)
#         name.delete(0, tk.END)
#         phone.delete(0, tk.END)

# def f_udalit():
#     ind = kniga.curselection()
#     if ind:
#         for i in reversed(ind):
#             kniga.delete(i)
#     else:
#         msg.showerror('error', 'вы ничего не выбрали')

# def f_udal_all():
#     kniga.delete(0, tk.END)

# pole_for_knopki = tk.Frame(window)
# pole_for_knopki.pack(pady=10)
# dobavit = tk.Button(pole_for_knopki, text='Добавить', command=f_dobavit)
# dobavit.pack(side=tk.LEFT, padx=15)
# udalit = tk.Button(pole_for_knopki, text='Удалить', command=f_udalit)
# udalit.pack(side=tk.LEFT, padx=15)
# udal_all = tk.Button(pole_for_knopki, text='Очистить всё', command=f_udal_all)
# udal_all.pack(side=tk.LEFT, padx=15)

# window.mainloop()


# #3
# import tkinter as tk
# import tkinter.messagebox as msg

# window = tk.Tk()
# window.geometry('500x300')

# okno_for_spiski = tk.Frame(window)
# okno_for_spiski.pack()
# spisok1 = tk.Listbox(okno_for_spiski, width=30)
# spisok1.pack(side=tk.LEFT, padx = 15)
# spisok2 = tk.Listbox(okno_for_spiski, width=30)
# spisok2.pack(side=tk.LEFT, padx = 15)

# okno_for_okna = tk.Frame(window)
# okno_for_okna.pack(pady = 20, fill='x')
# okno_for_part1 = tk.Frame(okno_for_okna)
# okno_for_part1.pack(side=tk.LEFT, expand=True, fill='x')
# okno_for_part2 = tk.Frame(okno_for_okna)
# okno_for_part2.pack(side=tk.LEFT, expand=True, fill='x')

# label1 = tk.Label(okno_for_part1, text='для списка 1')
# label1.pack(expand=True)
# label2 = tk.Label(okno_for_part2, text='для списка 2')
# label2.pack(expand=True)

# vvod1 = tk.Entry(okno_for_part1)
# vvod1.pack()
# vvod2 = tk.Entry(okno_for_part2)
# vvod2.pack()

# for_spisok1 = []
# for_spisok2 = []

# def dobavit_in_spisok_1():
#     a = vvod1.get()
#     if not a:
#         msg.showerror('error', 'Вы ничего не ввели')
#     else:
#         spisok1.insert(tk.END, a)
#         for_spisok1.append(a)
#         vvod1.delete(0, tk.END)

# def dobavit_in_spisok_2():
#     a = vvod2.get()
#     if not a:
#         msg.showerror('error', 'Вы ничего не ввели')
#     else:
#         spisok2.insert(tk.END, a)
#         for_spisok2.append(a)
#         vvod2.delete(0, tk.END)

# knopka1 = tk.Button(okno_for_part1, text = 'Добавить в список 1', command=dobavit_in_spisok_1, bg='green', font = ('Times New Roman', 10))
# knopka1.pack()
# knopka2 = tk.Button(okno_for_part2, text = 'Добавить в список 2', command=dobavit_in_spisok_2, bg='green', font = ('Times New Roman', 10))
# knopka2.pack()

# def f_sravnit():
#     in_1_but_not_in_2 = []
#     in_2_but_not_in_1 = []
    
#     for i in range(len(for_spisok1)):
#         if for_spisok1[i] not in for_spisok2:
#             in_1_but_not_in_2.append(for_spisok1[i])
#     for i in range(len(for_spisok2)):
#         if for_spisok2[i] not in for_spisok1:
#             in_2_but_not_in_1.append(for_spisok2[i])
#     if len(in_1_but_not_in_2)==0 and len(in_2_but_not_in_1)==0:
#         msg.showinfo('info', 'Списки одинаковые')
#     else:
#         new_okno = tk.Toplevel(window)
#         new_okno.title('Сравнение')
#         odinakovoe_li = tk.Label(new_okno, text='Не одинаковые')
#         odinakovoe_li.pack()
#         info_1 = tk.Label(new_okno, text=f'Есть в списке 1, но нет в списке 2:  {", ".join(in_1_but_not_in_2)}')
#         info_1.pack()
#         info_2 = tk.Label(new_okno, text=f'Есть в списке 2, но нет в списке 1:  {", ".join(in_2_but_not_in_1)}')
#         info_2.pack()
        

# sravnit = tk.Button(window, text = 'Сравнить', bg='purple', font = ('Times New Roman', 20), command=f_sravnit)
# sravnit.pack()

# window.mainloop()


#4
import tkinter as tk
import tkinter.messagebox as msg
from PIL import Image, ImageTk
import random

def igra(lives):
    window = tk.Tk()
    window.geometry('300x100')
    window.title('Давай поиграем???')

    fruits = ["яблоко", "банан", "апельсин", "груша", "киви", "манго", "ананас", "виноград", "персик", "слива", "абрикос", "лимон", "мандарин", "нектарин", "лайм", "гранат", "дыня", "папайя", "кокос", "карамбола", "маракуйя", "питайя", "фейхоа", "хурма"]
    school = ["учитель", "ученики", "класс", "учебник", "парты", "тетрадь", "карандаш", "ручка", "доска", "школа", "урок", "домашнее задание", "экзамен", "тест", "проект", "перерыв", "классная дверь", "расписание", "учебный год", "гимназия", "лицей", "столовая", "средняя школа", "начальная школа", "библиотека", "учебные материалы", "классный руководитель", "письменный стол", "мел", "лампа", "сумка", "учебные принадлежности", "школьная форма", "парта", "школьник", "училка", "классная доска", "школьная церемония", "олимпиада", "кружок", "экскурсия", "учебный план", "отметки", "достижения", "учебное заведение"]
    animals = ["слон", "тигр", "леопард", "жираф", "зебра", "носорог", "обезьяна", "шимпанзе", "горилла", "животное", "фламинго", "орёл", "сова", "утка", "кролик", "белка", "куница", "акула", "дельфин", "касатка", "морж", "морской котик", "осьминог", "красная рыба", "карась", "щука", "сом", "кабан", "олень", "лось", "заяц", "белка", "утконос", "панда", "кенгуру", "павлин", "фазан", "муха", "комар", "таракан", "жук", "мотылёк", "бабочка", "оса", "пчела", "улитка", "черепаха", "рыба клоун", "скат", "аксолотль", "пума", "ягуар", "барсук", "выдра", "бобр", "ёлочный ёж", "стриж", "воробей", "скворец", "ласточка", "филин", "скворец", "сурикат", "тюлень", "морская звезда", "медуза", "кальмар"]

    options = ["ничего", "фрукты", "школа", "животные"]
    vibrano = tk.StringVar(window)  # Переменная для хранения текущего выбранного значения
    vibrano.set(options[0])

    for_vibor = tk.Frame(window)
    for_vibor.pack()

    def start():
        poluchit = vibrano.get()
        if poluchit=='ничего':
            return 0
        else:
            knopka_vibora.destroy()
            window.geometry('900x700')
            
            window_for_img = tk.Toplevel(window)
            window_for_img.geometry('500x300')
            window_for_img.title('Смерть близко')
            
            for_img = tk.Label(window_for_img)
            for_img.pack()
            
            if poluchit=='фрукты':
                random_word = random.choice(fruits)
            elif poluchit=='школа':
                random_word = random.choice(school)
            elif poluchit=='животные':
                random_word = random.choice(animals)
            
            new_random_word = []
            for i in range(len(random_word)):
                if random_word[i]!=' ':
                    new_random_word.append('_')
                    new_random_word.append(' ')
                else:
                    new_random_word.append(' ')
                    new_random_word.append(' ')
            
            shifr = tk.Label(window, text = "".join(new_random_word), font = ('Times New Roman', 40))
            shifr.pack()
            
            def proverka(event = None):
                nonlocal new_random_word, kol_popitok, ispolzovano
                global lives
                
                letter = letter_entry.get()
                letter_entry.delete(0, tk.END)
                
                if letter=='дай мне луч надежды':
                    ricardooo = tk.Toplevel(window)
                    ricardooo.geometry('700x450')
                    ricardooo.title('РИКАРДОООООООО')
                    ricardooo_label = tk.Label(ricardooo)
                    ricardooo_label.pack()
                    
                    img = Image.open('img_for_laba13/рикардо.jpg')
                    img = img.resize((700, 450))
                    photo = ImageTk.PhotoImage(img)
                    
                    ricardooo_label.photo = photo
                    ricardooo_label.config(image = photo)
                    
                if len(letter)==1 and 'а'<=letter<='я':
                    if letter not in ispolzovano:
                        if letter in random_word:
                            for i in range(len(random_word)):
                                if letter==random_word[i]:
                                    new_random_word[2*i] = letter
                            shifr.config(text = "".join(new_random_word))
                            ispolzovano.append(letter)
                            ispolzovano_label.config(text = f'Буквы использованы: {" ".join(ispolzovano)}')
                        else:
                            kol_popitok-=1
                            kol_popitok_label.config(text = f'Количество попыток: {kol_popitok}')
                            ispolzovano.append(letter)
                            ispolzovano_label.config(text = f'Буквы использованы: {" ".join(ispolzovano)}')
                    else:
                        msg.showerror('Предупреждение!', 'Эта буква уже использована')
                else:
                    if letter!='дай мне луч надежды':
                        msg.showerror('Предупреждение!', 'Буква не заглавная или букв несколько. Или это не буква...')
                    return 0
                if kol_popitok==5:
                    img = Image.open('img_for_laba13/деньги_застройщику.jpg')
                    img = img.resize((500, 300))
                    photo = ImageTk.PhotoImage(img)
                    for_img.photo = photo
                    for_img.config(image=photo)
                elif kol_popitok==4:
                    img = Image.open('img_for_laba13/доски.bmp')
                    img = img.resize((500, 300))
                    photo = ImageTk.PhotoImage(img)
                    for_img.photo = photo     
                    for_img.config(image=photo)
                elif kol_popitok==3:
                    img = Image.open('img_for_laba13/стройка.jpg')
                    img = img.resize((500, 300))
                    photo = ImageTk.PhotoImage(img)
                    for_img.photo = photo     
                    for_img.config(image=photo)
                elif kol_popitok==2:
                    img = Image.open('img_for_laba13/готово.jpg')
                    img = img.resize((500, 300))
                    photo = ImageTk.PhotoImage(img)
                    for_img.photo = photo     
                    for_img.config(image=photo)
                elif kol_popitok==1:
                    img = Image.open('img_for_laba13/палач.jpg')
                    img = img.resize((500, 300))
                    photo = ImageTk.PhotoImage(img)
                    for_img.photo = photo     
                    for_img.config(image=photo)
                elif kol_popitok==0:
                    img = Image.open('img_for_laba13/смерть.webp')
                    img = img.resize((500, 300))
                    photo = ImageTk.PhotoImage(img)
                    for_img.photo = photo     
                    for_img.config(image=photo)
                    
                    msg.showerror('Вы умерли', 'Вы умерли')
                    lives = 0
                    window.destroy()
                if new_random_word.count('_')==0:
                    msg.showinfo('Удача на вашей стороне', 'Вы чудом выжили')
                    window.destroy()
            
            kol_popitok = 6
            kol_popitok_label = tk.Label(window, text = f'Количество попыток: {kol_popitok}', font = ('Times New Roman', 24))
            kol_popitok_label.pack(padx = 20, pady = 20)
            ispolzovano = []
            ispolzovano_label = tk.Label(window, text = f'Буквы использованы: {" ".join(ispolzovano)}', font = ('Times New Roman', 20))
            ispolzovano_label.pack(padx = 20, pady = 20)
            letter_label = tk.Label(window, text = 'Введите букву:', font = ('Times New Roman', 24))
            letter_label.pack(padx = 20, pady = 20)
            letter_entry = tk.Entry(window, font = ('Times New Roman', 20))
            letter_entry.pack(padx = 20, pady = 5)
            letter_entry.bind('<Return>', proverka)
            proverit_button = tk.Button(window, text = 'Проверить', bg = 'green', font = ('Times New Roman', 20), command = proverka)
            proverit_button.pack(padx = 20, pady = 10)
        
    dropdown = tk.OptionMenu(for_vibor, vibrano, *options)
    dropdown.pack(padx=20, pady=20, side=tk.LEFT)
    knopka_vibora = tk.Button(for_vibor, text="Выбрать", bg='green', command=start)
    knopka_vibora.pack(pady=10, side=tk.LEFT)

    window.mainloop()
    
lives = 1
while lives==1:
    igra(lives)