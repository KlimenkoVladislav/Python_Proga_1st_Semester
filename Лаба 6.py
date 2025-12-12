#1
# import random
# a = []
# while len(a)!=6:
#     n = random.randint(1, 49)
#     if n not in a:
#         a.append(n)
# for i in range(len(a)):
#     print(a[i], end=' ')

#2
# a = list(map(int, input().split()))
# print('________________')
# while True:
#     a_new_week = list(map(int, input().split()))
#     for i in range(5): #можно вводить сколько хочешь, но обрабатываться будут только 5 элементов
#         if a_new_week[i]>a[i]:
#             print(i+1, end=' ')
#             a[i] = a_new_week[i]
#     if int(input('      Хотите продолжить (0/1)? '))==0:
#         break
#     else:
#         print('________________')

#3
# rost = int(input())
# stroi = list(map(int, input().split()))
# for i in range(len(stroi)-1):
#     if stroi[i]<stroi[i+1]:
#         print('что за фигня?')
#         break
# for i in range(len(stroi)):
#     if rost>stroi[i]:
#         print(i+1)
#         break
# else:
#     print(len(stroi)+1)

#4
# import random
# popitki, kol = 0, 0
# a = ''
# while ('OOO' not in a) and ('PPP' not in a):
#     popitki+=1
#     a+=random.choice('OP')
# print(a, popitki)

#5
# depths = list(map(int, input().strip().split()))
# indexi = []
# maxx = -99999
# for i in range(len(depths)):
#     if i!=0 and i!=len(depths)-1:
#         if depths[i-1]<depths[i] and depths[i]>depths[i+1]:
#             indexi.append(i)
#     if i in indexi and depths[i]>maxx:
#         maxx = depths[i]
# if len(indexi)==0:
#     print('кладов нет')
# else:
#     depths.remove(maxx)
#     print(indexi, maxx, depths)

#6
# a = input().strip()
# summa = 0
# for i in range(1, len(a)+1):
#     if i%2==0:
#         summa+=int(a[i-1])
#     else:
#         if int(a[i-1])*2>9:
#             summa+=int(a[i-1])*2-9
#         else:
#             summa+=int(a[i-1])*2
# if summa%10==0:
#     print('Normal`no')
# else:
#     print('Ne normal`no')

#7
# a = int(input('Сколько строк вы хотите ввести? '))
# otv = []
# for i in range(a):
#     slovo = input().strip()
#     if len(slovo)>10:
#         otv.append(slovo[0] + str(len(slovo)-2) + slovo[-1])
#     else:
#         otv.append(slovo)
# for i in range(len(otv)):
#     print(otv[i], end='\n')

#8
# a = int(input('Введите количество комнат: '))
# kol=0
# for i in range(a):
#     n = list(map(int, input().strip().split()))
#     if len(n)!=2 or n[0]>n[1]:
#         print('переделывай')
#         break
#     elif n[0]+2<=n[1]:
#         kol+=1
# print(kol)