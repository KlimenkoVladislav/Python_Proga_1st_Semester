# #0
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import math

# x = []
# y = []
# for i in range(4):
#     y.append(-0.25 * i + 1)
#     x.append(i)

# for i in range(4,10):
#     x.append(i)
#     y.append((i-4)/3)

# for i in range(10,14):
#     x.append(i)
#     y.append(2 + 0.6 * math.sin(3.14/2 * (i - 10)))

# for i in range(14,21):
#     x.append(i)
#     y.append(0.5/6 * (i - 14) + 2)

# fig, ax = plt.subplots()

# line = ax.plot([],[])[0]

# def animation(frame):
#     x_animation = x[:frame +1]
#     y_animation = y[:frame +1]
#     line.set_data(x_animation,y_animation)
#     return line,

# ani = FuncAnimation(fig,animation,frames=30,interval=100, repeat=True)
# ax.set_xlim(0,20)
# ax.set_ylim(0,5)
# plt.show()

# #1
# import matplotlib.pyplot as plt
# import random

# name = []
# rost = []
# colors = []
# kol_name = int(input('Данные о каком количестве человек вы хотите ввести? '))
# y = []
# for i in range(kol_name):
#     a = input('Введите имя и рост (через пробел): ').split()
#     name.append(a[0])
#     rost.append(int(a[1]))
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     colors.append((r, g, b))
#     plt.text(i, rost[i]-rost[i]/2, str(rost[i]))

# plt.bar(name, rost, color = colors)
# plt.xlabel('Имена друзей', color = 'red')
# plt.ylabel('Рост моих друзей', color = 'red')
# plt.title('Рост (см)', color = 'red')
# figsize=(8, 5)

# plt.show()

# #2
# import matplotlib.pyplot as plt
# import random

# energy = 100
# nastroenie = 50
# graf_energy = []
# graf_nastroenie = []
# h = []
# events = [
#     ["Питомец вспомнил хороший день", 10],
#     ["Нашёл конфету", 15],
#     ["Увидел бабочку", 8],
#     ["Захотел танцевать", 12]
# ]

# for hour in range(1, 25):
#     h.append(hour)
#     energy-=5
#     nastroenie-=5
#     a = random.randint(1, 10)
#     if a==1:
#         a = random.randint(0, 3)
#         print(events[a])
#         nastroenie+=events[a][1]
#     if hour==9 or hour==14 or hour==19:
#         energy+=10
#     if energy>100:
#         energy=100
#     if energy<0:
#         energy=0
#     if nastroenie>100:
#         nastroenie=100
#     if nastroenie<0:
#         nastroenie=0
#     graf_energy.append(energy)
#     graf_nastroenie.append(nastroenie)

# plt.plot(h, graf_energy, color = 'red', label = 'energy')
# plt.plot(h, graf_nastroenie, color = 'blue', label = 'nastroenie')
# plt.title('Симулятор питомца Тамагочи')
# plt.xlabel('Часы')
# plt.ylabel('Количество энергии и настроения')
# plt.xlim(0, 24)
# plt.ylim(0, 100)

# plt.show()

#3
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

x = [0]
y = [0]
kol_shagov = int(input('Введите количество шагов: '))
for i in range(kol_shagov):
    a = random.randint(0, 3)
    if a==0: 
        x.append(x[-1]+1)
        y.append(y[-1])
    if a==1: 
        x.append(x[-1]-1)
        y.append(y[-1])
    if a==2: 
        y.append(y[-1]+1)
        x.append(x[-1])
    if a==3: 
        y.append(y[-1]-1)
        x.append(x[-1])

fig, ax = plt.subplots()

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(which='both')

line, = plt.plot([], [], color='blue')
plt.xlim(min(x)-1, max(x)+1)
plt.ylim(min(y)-1, max(y)+1)

def animation(frame):
    if frame>=len(x):
        frame = len(x)-1
    x_animation = x[:frame +1]
    y_animation = y[:frame +1]
    line.set_data(x_animation,y_animation)
    return line,

ani = FuncAnimation(fig, animation, frames=len(x), interval=100, repeat=False)

plt.show()