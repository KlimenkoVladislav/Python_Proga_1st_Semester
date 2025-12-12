spisok_failov = ['не файл для смещения индекса на 1', 'file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt', 'file6.txt']

#1
# f = open(spisok_failov[2], encoding='utf8')
# text = [s.split() for s in f]
# maxx = 0
# maxx_2, name_2 = 0, ''
# for stroka in text:
#     if int(stroka[2])>maxx:
#         maxx = int(stroka[2])
# for stroka in text:
#     if int(stroka[2])>maxx_2 and int(stroka[2])!=maxx:
#         maxx_2 = int(stroka[2])
#         name_2 = stroka[0] + ' ' + stroka[1]
# print(name_2, maxx_2)
# f.close()       

#2
# for i in range(3, 5):
#     f = open(spisok_failov[i], encoding = 'utf8')
#     text = f.read().split()
#     for slovo in text:
#         if slovo == 'Academy':
#             print(spisok_failov[i])
#             break
#     f.close()

#3
# f = open(spisok_failov[4], encoding = 'utf8')
# kol_slov_with_e = 0
# text = f.read().split()
# for i in range(len(text)):
#     for bukva in text[i]:
#         if bukva == 'e':
#             kol_slov_with_e+=1
#             break 
# print(kol_slov_with_e/len(text)*100, '%')
# f.close()

#4
# a = int(input('Введите количество имён: '))
# g = input('Мужские именя или женские (M/W)? ')
# imena = 0
# if g.lower()=='m':
#     f = open(spisok_failov[6], encoding = 'utf8')
# else:
#     f = open(spisok_failov[5], encoding = 'utf8')
# for stroka in f:
#     stroka = stroka.split()
#     print(stroka[0])
#     imena+=1
#     if imena==a:
#         break 
# f.close()

#5
# a = input()
# with open('file_for_task_E.txt', 'r', encoding='utf8') as f:
#     text = f.readlines()
#     text.insert(len(text)//2, a+'\n')
# with open('file_for_task_E.txt', 'w', encoding='utf8') as f:
#     for i in range(len(text)):
#         f.write(text[i])

#6          это и для шифрования и для дешифрования
# with open('file_for_task_F.txt', 'r', encoding='utf8') as f:
#     for stroka in f:
#         stroka = stroka.split()
#         for i in range(len(stroka)):
#             stroka[i] = stroka[i][::-1]
#             print(stroka[i], end=' ')
#         print('')

#7
# import random
# parol = ''
# with open(spisok_failov[3], 'r', encoding='utf8') as f:
#     text = f.read().split()
#     while len(parol)<8 or len(parol)>10:
#         parol = ''
#         for i in range(2):
#             a = ''
#             while len(a)<3:
#                 a = random.choice(text)
#                 if a[-1].isalpha() == False:
#                     a = a[:-1]
#             parol+=a.capitalize()
#     print(parol)

#8
# while True:
#     a = int(input('Количество строк: '))
#     if a%2==1:
#         break
# b = int(input('Количеслво столбцов: '))
# for i in range(a):
#     if i%2==0:
#         print('#'*b)
#     else:
#         if i%4==1:
#             print('.'*(b-1)+'#')
#         elif i%4==3:
#             print('#'+'.'*(b-1))