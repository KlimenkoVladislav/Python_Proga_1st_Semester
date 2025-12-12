#7
# import random
# you, opp = 0, 0
# st = ['st', 'stone', 'камень', 'к']
# sc = ['sc', 'scissors', 'ножницы', 'н']
# p = ['p', 'paper', 'бумага', 'б']
# while you!=3 and opp!=3:
#     n = random.randint(1, 3) #1 - камень, 2 - ножницы, 3 - бумага
#     a = input()
#     if a in st and n == 2:
#         you += 1
#     elif a in st and n == 3:
#         opp += 1
#     if a in sc and n == 3:
#         you += 1
#     elif a in sc and n == 1:
#         opp += 1
#     if a in p and n == 3:
#         you += 1
#     elif a in p and n == 2:
#         opp += 1
#     print('you - ', you, '| opponent - ', opp)

#8
# a = input('Введите строку: ')
# kol_bukv, kol_cfir, kol_probel, kol_ost=0, 0, 0, 0
# print('Количество символов: ', len(a))
# for i in a:
#     if i.isalpha():
#         kol_bukv+=1
#     elif i.isdigit():
#         kol_cfir+=1
#     elif i==' ':
#         kol_probel+=1
#     else:
#         kol_ost+=1
# print('Количество букв: ', kol_bukv)
# print('Колическто цифр: ', kol_cfir)
# print('Количество пробелов: ', kol_probel)
# print('Количество остальных символов: ', kol_ost)

# a = a.lower()
# b = a[0]
# a = a.replace(a[0], b.upper(), 1)
# print(a)
# a_new = ''
# for i in a:
#     if i in 'аеёиоуыэюяАЕЁИОУЫЭЮЯ':
#         a_new+='*'
#     else:
#         a_new+=i
# print(a_new)

# b = input('Введите то, что хотите найти: ')
# print('Количество вхождений: ', a.count(b))
# if a.count(b)>0:
#     print('Найдено')
# else:
#     print('Не найдено')
# c = input('Введите, то на что хотите заменить: ')
# print(a.replace(b, c))

# print('Количество слов: ', a.replace('  ', ' ').replace('  ', ' ').strip().count(' ')+1)
# maxx = 0
# kol = 0
# maxx_word = ''
# for i in range(len(a)):
#     if a[i]!=' ' and i!=len(a)-1:
#         kol+=1
#     else:
#         if maxx<kol:
#             maxx = kol
#             maxx_word=str(a[i-maxx: i+1])
#         kol = 0
# print('Самое длинное слово: ', maxx_word)

# if a.isalpha():
#     print('Строка состоит только из букв')
# else:
#     print('Строка состоит не только из букв')
# if a.isdigit():
#     print('Строка состоит только из цифр')
# else:
#     print('Строка состоит не только из цифр')
# if a[-1]=='.' or a[-1]=='!' or a[-1]=='?':
#     print('Строка заканчивается точкой, восклицательным или вопросительным знаком')
# else:
#     print('Строка не заканчивается точкой, восклицательным или вопросительным знаком')

#9
a = input('Введите строку: ')
sm = int(input('Введите смещение (оно должно попадать в промедуток [-51; 51]): '))
op = int(input('Введите номер операции, где 1 - это зашифровать, а 2 - расшифровать: '))
ack = 0
if -52<sm<52:
    while ack == 0:
        a_new = ''
        for i in range(len(a)):
            if a[i].isalpha():
                if 65<=ord(a[i])<=90 and 65<=ord(a[i])+sm<=90:
                    a_new+=chr(ord(a[i])+sm)
                elif 65<=ord(a[i])<=90 and 65>ord(a[i])+sm:
                    a_new+=chr(26+ord(a[i])+sm)
                elif 65<=ord(a[i])<=90 and ord(a[i])+sm>90:
                    a_new+=chr(-26+ord(a[i])+sm)
                if 97<=ord(a[i])<=122 and 97<=ord(a[i])+sm<=122:
                    a_new+=chr(ord(a[i])+sm)
                elif 97<=ord(a[i])<=122 and 97>ord(a[i])+sm:
                    a_new+=chr(26+ord(a[i])+sm)
                elif 97<=ord(a[i])<=122 and ord(a[i])+sm>122:
                    a_new+=chr(-26+ord(a[i])+sm)
            else:
                a_new+=a[i]
        if op == 1:
            print(a_new)
            ack=1
        if op == 2:
            print(a_new)
            sm+=1
            ack = int(input('Вас устроивает данная строка? 1 - да, 0 - нет: '))
else:
    sm = int(input('Введите смещение (оно должно попадать в промедуток [-51; 51]): '))
