# 1
# import matplotlib.pyplot as plt

# x = ['Маргарита Мания', 'ПепперониПарад', 'Гавайский Хаос', 'Четыре Сыра и Слёзы', '«Веганский Бунт']
# y = [23, 45, 56, 78, 32]
# plt.bar(x, y, color = None)
# plt.xlabel('Пиццерии', color = 'red')
# plt.ylabel('Продано пицц', color = 'red')
# plt.title('Битва пиццерий: Кто продал больше всего пицц?', color = 'red')

# plt.legend()
# plt.show()

# 2
# import matplotlib.pyplot as plt

# sizes = [8, 7, 5, 4]
# dela = ['мир спасает', 'дрыхнет', 'кибер развлекаловка', 'другое (все мы знаем, что он поедает дошик)']
# plt.pie(sizes, labels=dela, autopct='%1.1f%%', startangle=0)
# plt.title('День супергероя', color = 'red')

# plt.legend()
# plt.show()

# 3
# import matplotlib.pyplot as plt
# import random 

# x = [random.randint(0, 1) for i in range(1000)]

# plt.hist(x, edgecolor = None, color = None)
# plt.grid(axis='y')
# plt.xlabel('распределение по росту', color='red')
# plt.ylabel('количество мутантов данного роста', color='red')
# plt.title('рост 1000 монстров', color='red')

# plt.show()

# 4
import matplotlib.pyplot as plt

month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
kol = [0]*12
animals = ['Олени', 'Кабаны', 'Лисы']
kol_animals = [0, 0, 0]
detections = -1
with open('5.txt', 'r', encoding='utf8') as file:
    for stroka in file:
        if detections<0:
            detections=0
            continue
        stroka = stroka.split(';')
        if stroka[2][0].isdigit()==False:
            continue
        detections+=int(stroka[2])
        for i in range(12):
            if stroka[0][:-5] == month[i]:
                kol[i]+=int(stroka[2])
        for i in range(3):
            if stroka[1]==animals[i]:
                kol_animals[i]+=int(stroka[2])
print('Самый заметный вид: ', animals[kol_animals.index(max(kol_animals))])
spad = []
for i in range(11):
    spad.append(kol[i]-kol[i+1])
print(spad)
print('Месяц с наибольшим спадом: ', month[spad.index(max(spad))+1])

plt.bar(month, kol, color = None)
plt.title('Активность животных по месяцам', color = 'red')
plt.xlabel('Месяца', color = 'red')
plt.ylabel('Количество', color = 'red')

plt.show()