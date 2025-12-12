# #1
# import string

# while 1:
#     n = int(input('Введите число: '))
#     if 1<=n<=100:
#         break
#     else:
#         print('Число должно быть больше 0 и меньше 101')
# kol_captains = 0
# list_of_people = []
# for i in range(n):
#     correct = 1
#     stroka = input()
#     for i in range(len(stroka)):
#         kol_probekov = 0
#         if i==0:
#             if not 'A'<=stroka[0]<='Z' and stroka[0]!=' ':
#                 correct = 0
#                 break
#         else:
#             if not 'a'<=stroka[i]<='z' and stroka[i]!=' ':
#                 correct = 0
#                 break
#         if stroka[i] not in string.ascii_letters:
#             if stroka[i] == ' ':
#                 kol_probekov+=1
#                 if kol_probekov>1:
#                     correct = 0
#                     break
#                 continue
#             else:
#                 correct = 0
#                 break
#     if correct==0:
#         print('Некорректная строка')
#         break
#     stroka = stroka.split()
#     if not (1<=len(stroka[0])<=10) or stroka[1] not in ['woman', 'child', 'man', 'captain']:
#         print('Некорректная строка')
#         break
#     if stroka[1] == 'captain':
#         kol_captains+=1
#     if kol_captains>1:
#         print('Неправильное количество капитанов')
#         break
#     list_of_people.append(stroka)
# if kol_captains==0:
#     print('Неправильное количество капитанов')
#     list_of_people = []
# if len(list_of_people):
#     for i in range(len(list_of_people)):
#         if list_of_people[i][1] == 'woman' or list_of_people[i][1] == 'child':
#             print(list_of_people[i][0])
#     for i in range(len(list_of_people)):
#         if list_of_people[i][1] == 'man':
#             print(list_of_people[i][0])
#     for i in range(len(list_of_people)):
#         if list_of_people[i][1] == 'captain':
#             print(list_of_people[i][0])
#             break


# #2
# while 1:
#     k = int(input('Введите число: '))
#     if 1<=k<=100:
#         break
#     else:
#         print('Число должно быть больше 0 и меньше 101')
# spisok_mes = []
# first_is_plus = 1
# for i in range(k):
#     mes = input('+ — сообщение от клиента (вопрос); - — сообщение от специалиста (ответ)    ')
#     if i==0 and mes!='+':
#         print('Первым должен связаться клиент')
#         first_is_plus = 0
#         break
#     if len(mes)!=1 or (mes!='+' and mes!='-'):
#         print('Неверные данные')
#         break
#     spisok_mes.append(mes)
# if first_is_plus==1:
#     kol_mes_from_user = 0
#     kol_mes_from_spets = 0
#     for i in range(len(spisok_mes)):
#         if spisok_mes[i]=='+':
#             kol_mes_from_user+=1
#         else:
#             kol_mes_from_spets+=1
#         if kol_mes_from_spets>kol_mes_from_user:
#             print('Ненорм')
#             break
#         if i==len(spisok_mes)-1:
#             if kol_mes_from_user==kol_mes_from_spets:
#                 print('Норм')
#             else:
#                 print('Ненорм')


#3
import tkinter as tk
import random
from PIL import Image, ImageTk, ImageSequence

def weather():
    global photo1
    w = ['Солнечно', 'Дождь', 'Облачно', 'Снег']
    a = random.choice(w)
    text.config(text = a)
    if a == 'Солнечно':
        window.config(bg = 'yellow')
        img1 = Image.open('img_and_gif_for_laba12/sun.bmp')
        img1 = img1.resize((340, 165))
        photo1 = ImageTk.PhotoImage(img1)
        label_for_photo1.config(image=photo1)
        label_for_photo2.config(image=photo1)
    elif a == 'Дождь':
        window.config(bg = 'blue')
        img1 = Image.open('img_and_gif_for_laba12/rain.png')
        img1 = img1.resize((340, 165))
        photo1 = ImageTk.PhotoImage(img1)
        label_for_photo1.config(image=photo1)
        label_for_photo2.config(image=photo1)
    elif a == 'Облачно':
        window.config(bg = 'grey')
        img1 = Image.open('img_and_gif_for_laba12/oblaka.jpg')
        img1 = img1.resize((340, 165))
        photo1 = ImageTk.PhotoImage(img1)
        label_for_photo1.config(image=photo1)
        label_for_photo2.config(image=photo1)
    else:
        window.config(bg = 'white')
        img1 = Image.open('img_and_gif_for_laba12/snow.jpg')
        img1 = img1.resize((340, 165))
        photo1 = ImageTk.PhotoImage(img1)
        label_for_photo1.config(image=photo1)
        label_for_photo2.config(image=photo1)

window = tk.Tk()
window.title('Погода')

knopka = tk.Button(window, text = 'Сгенерировать случайную погоду', font = ('Times New Roman', 40), command = weather, bg = 'purple')
knopka.grid(row = 0, column=0, columnspan=2, padx = 30, pady = 20)

text = tk.Label(window, text = 'Погода', font = ('Times New Roman', 24))
text.grid(row = 1, column=0, columnspan=2)

label_for_photo1 = tk.Label(window)
label_for_photo1.grid(row = 2, column=0, sticky='w')
label_for_photo2 = tk.Label(window)
label_for_photo2.grid(row = 2, column=1, sticky='e')

gif = Image.open('img_and_gif_for_laba12/pocoyo_dance.gif')
label = tk.Label(window)
label.grid(row = 2, column=0, columnspan=2,  pady = 50)
frames = []
for frame in ImageSequence.Iterator(gif):   # Извлекаем все кадры
    frames.append(ImageTk.PhotoImage(frame.convert('RGBA')))

def animate(counter=0):
    label.config(image=frames[counter])
    counter = (counter + 1) % len(frames)    # следующий кадр
    window.after(50, animate, counter)    # вызываем функцию после 50 мс

animate()
tk.mainloop()


# #4
# import tkinter as tk
# from PIL import Image, ImageTk

# def konv():
#     r = int(vvod.get())
#     res1.config(text=f"{r*0.012654:.2f}")
#     res2.config(text=f"{r*0.011042:.2f}")
#     res3.config(text=f"{r*0.009664:.2f}")
#     res4.config(text=f"{r*1.99:.2f}")

# window = tk.Tk()
# window.title('Конвертирование валют')
# window.geometry('570x500')

# knopka = tk.Button(window, text = 'Конвертировать', command = konv, bg='green', font=('Times New Roman', 28))
# knopka.grid(row=5, column=0, columnspan=3)

# label0 = tk.Label(window, text='Рубли: ', font=('Times New Roman', 20))
# label0.grid(padx=20, pady=20, row=0, column=0, sticky='w')
# label1 = tk.Label(window, text='USD: ', font=('Times New Roman', 20))
# label1.grid(padx=20, pady=20, row=1, column=0, sticky='w')
# label2 = tk.Label(window, text='EUR: ', font=('Times New Roman', 20))
# label2.grid(padx=20, pady=20, row=2, column=0, sticky='w')
# label3 = tk.Label(window, text='GBP: ', font=('Times New Roman', 20))
# label3.grid(padx=20, pady=20, row=3, column=0, sticky='w')
# label4 = tk.Label(window, text='JPY: ', font=('Times New Roman', 20))
# label4.grid(padx=20, pady=20, row=4, column=0, sticky='w')

# res1 = tk.Label(window, text = '0', font=('Times New Roman', 20))
# res1.grid(padx=20, pady=20, row=1, column=1)
# res2 = tk.Label(window, text = '0', font=('Times New Roman', 20))
# res2.grid(padx=20, pady=20, row=2, column=1)
# res3 = tk.Label(window, text = '0', font=('Times New Roman', 20))
# res3.grid(padx=20, pady=20, row=3, column=1)
# res4 = tk.Label(window, text = '0', font=('Times New Roman', 20))
# res4.grid(padx=20, pady=20, row=4, column=1)

# vvod = tk.Entry(window, font=('Times New Roman', 20))
# vvod.grid(padx=20, pady=20, row=0, column=1)

# img_ru = Image.open('img_and_gif_for_laba12/РОССИЯ.jpg')
# img_ru = img_ru.resize((95, 66))
# flag_ru = ImageTk.PhotoImage(img_ru)
# label_for_flag_ru = tk.Label(window, image=flag_ru)
# label_for_flag_ru.grid(row=0, column=2, sticky='e')

# img_usa = Image.open('img_and_gif_for_laba12/usa.png')
# img_usa = img_usa.resize((50, 30))
# flag_usa = ImageTk.PhotoImage(img_usa)
# label_for_flag_usa = tk.Label(window, image=flag_usa)
# label_for_flag_usa.grid(row=1, column=2, sticky='e')

# img_eur = Image.open('img_and_gif_for_laba12/eur.png')
# img_eur = img_eur.resize((50, 30))
# flag_eur = ImageTk.PhotoImage(img_eur)
# label_for_flag_eur = tk.Label(window, image=flag_eur)
# label_for_flag_eur.grid(row=2, column=2, sticky='e')

# img_gbp = Image.open('img_and_gif_for_laba12/gbp.jpg')
# img_gbp = img_gbp.resize((50, 30))
# flag_gbp = ImageTk.PhotoImage(img_gbp)
# label_for_flag_gbp = tk.Label(window, image=flag_gbp)
# label_for_flag_gbp.grid(row=3, column=2, sticky='e')

# img_jpy = Image.open('img_and_gif_for_laba12/jpy.png')
# img_jpy = img_jpy.resize((50, 30))
# flag_jpy = ImageTk.PhotoImage(img_jpy)
# label_for_flag_jpy = tk.Label(window, image=flag_jpy)
# label_for_flag_jpy.grid(row=4, column=2, sticky='e')

# tk.mainloop()