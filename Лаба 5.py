# #6
# import random
# import string
# a = int(input('Введите количество символов в пароле: '))
# al = ''
# parol = ''
# if input('Нужны заглавные буквы? ').lower() == 'да':
#     al+=string.ascii_uppercase
# if input('Нужны строчные буквы? ').lower() == 'да':
#     al+=string.ascii_lowercase
# if input('Нужны цифры? ').lower() == 'да':
#     al+=string.digits
# if input('Нужны специальные символы? ').lower() == 'да':
#     al+=string.punctuation
# for i in range(a):
#     parol+=random.choice(al)
# print(parol)

#7
# a = input().replace('-', ':').split(':')
# if int(a[1][-1]) == int(a[2]):
#     print('Ничья')
# elif int(a[1][-1]>a[2]):
#     print(a[0])
# else:
#     print(a[1][:-2])