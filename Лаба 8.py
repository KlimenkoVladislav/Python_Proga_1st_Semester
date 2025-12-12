# # Лабораторная работа 8
# # Задание A: Автомобильные номера региона X

# import random
# import string

# def generate_license_plate():
#     """
#     Генерирует случайный автомобильный номер
#     """
#     nomer = []
#     b = string.ascii_uppercase
#     c = string.digits
#     a = random.randint(0, 1)
#     if a==0:
#         nomer+=random.choices(b, k=3)
#         nomer+=random.choices(c, k=3)
#     else:
#         nomer+=random.choices(c, k=4)
#         nomer+=random.choices(b, k=3)
#     return "".join(nomer)

# if __name__ == "__main__":
#     for i in range(1, 6):
#         print(f"Тест {i}: {generate_license_plate()}")

# # Лабораторная работа 8
# # Задание B: Магические даты XX века

# def is_magic_date(day, month, year):
#     """
#     Проверяет, является ли дата магической
#     """
#     if int(str(year)[2:]) == day*month:
#         print(day, month, year)

# if __name__ == "__main__":
#     for year in range(1901, 2001):
#         for month in range (1, 13):
#             if month in [1, 3, 5, 7, 8, 10, 12]:
#                 for day in range(1, 32):
#                     is_magic_date(day, month, year)
#             elif month in [4, 6, 9, 11]:
#                 for day in range(1, 31):
#                     is_magic_date(day, month, year)
#             else:
#                 for day in range(1, 29):
#                     is_magic_date(day, month, year)

# # Лабораторная работа 8
# # Задание C: Кулинарные меры

# def reduce_measure(amount, unit):
#     """
#     Преобразует меры объема
#     """
#     if amount<0 or ('.' in str(amount)) or not (unit in ['teaspoons', 'cups', 'tablespoons']):
#         return "Error"
#     if unit=='teaspoons':
#         return str(amount//16) + ' cups ' + str((amount%16)//3) + ' tablespoons ' + str((amount%16)%3) + ' teaspoons '
#     if unit=='cups':
#         return str(amount) + ' 0 tablespoons 0 teaspoons'
#     if unit=='tablespoons':
#         return str(amount//16) + ' cups ' + str(amount%16) + ' tablespoons ' + '0 reaspoons'

# if __name__ == "__main__":
#     print("59 teaspoons (корректный):", reduce_measure(59, "teaspoons"))
#     print("16 tablespoons (корректный):", reduce_measure(16, "tablespoons"))
#     print("3 teaspoons (корректный):", reduce_measure(3, "teaspoons"))
#     print("-5 cups (некорректный):", reduce_measure(-5, "cups"))
#     print("0 teaspoons (корректный):", reduce_measure(0, "teaspoons"))
#     print("3.5 cups (некорректный):", reduce_measure(3.5, "cups"))
#     print("2 liters (некорректная единица):", reduce_measure(2, "liters"))

# Лабораторная работа 8
# Задание D: Кнопочный телефон

# def text_to_phone_keys(text):
#     alf = [' ','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ'] #это является аналогичной словарю структурой потому что каждая буква соответствует своим индексам
#     numbers = ''
#     """
#     Преобразует текст в последовательность нажатий
#     """
#     for bukva in text.upper():
#         for i in range(len(alf)):
#             for j in range(len(alf[i])):
#                 if bukva == alf[i][j]:
#                     numbers+=str(i)*(j+1)
#     return numbers
    

# if __name__ == "__main__":
#     print("Hello, World!:", text_to_phone_keys("Hello, World!"))
#     print("ABC:", text_to_phone_keys("ABC"))
#     print("Hi!:", text_to_phone_keys("Hi!"))
#     print("aB c:", text_to_phone_keys("aB c"))
#     print("Python:", text_to_phone_keys("Python"))
#     print("Test 123:", text_to_phone_keys("Test 123"))

# Лабораторная работа 8
# Задание E: Доставка

# def decode_postal_code(code):
#     L1 = {'A': 'Солнечный берег',
#           'B': 'Зелёные холмы',
#           'C': 'Изумрудная долина',
#           'E': 'Киберсити',
#           'G': 'Жемчужный берег',
#           'H': 'Туманный лес',
#           'J': 'Пламенный утёс',
#           'K': 'Звёздный ручей',
#           'L': 'Солнечная гавань',
#           'M': 'Лунная роща'}
#     """
#     Декодирует четырехзначный почтовый код региона Канадория
#     """
#     if len(code)==0:
#         return 'пусто'
#     if len(code)!=4:
#         return 'error'
#     if code[0] not in L1:
#         return 'error'
#     if not (code[1].isdigit() and code[3].isdigit()):
#         return 'error'
    
#     if 1<=int(code[1])<=9:
#         a = 'Сельская местность'
#     elif int(code[1])==0:
#         a = 'Город'
#     if ord(code[2])<=ord('M'):
#         b = 'Основное отделение'
#     elif ord(code[2])>=ord('N'):
#         b = 'Дополнительное отделение'
#     if 0<=int(code[3])<=2:
#         c = 'Стандартная'
#     elif 3<=int(code[3])<=6:
#         c = 'Ускоренная'
#     else:
#         c = 'Экспресс'
#     return f"""
#         Регион: {L1[code[0]]},
#         Тип населённого пункта: {a},
#         Тип почтового отделения: {b},
#         Скорость доставки: {c}"""
    
# if __name__ == "__main__":
#     print("A2N1 (корректный):", decode_postal_code("A2N1"))
#     print("E0A7 (корректный):", decode_postal_code("E0A7"))
#     print("Z1A2 (некорректная буква):", decode_postal_code("Z1A2"))
#     print("A2N (некорректная длина):", decode_postal_code("A2N"))
#     print("1234 (некорректный формат):", decode_postal_code("1234"))
#     print("A2N12 (некорректная длина):", decode_postal_code("A2N12"))
#     print("a2n1 (нижний регистр):", decode_postal_code("a2n1"))
#     print(" (пустая строка):", decode_postal_code(""))

# Лабораторная работа 8
# Задание F: Эрудит - Битва Саши Ш.

# def calculate_scrabble_score(word):
#     """
#     Вычисляет количество очков в игре Эрудит для русского слова
#     """
#     da_kakoi_blin_slovar = {
#         'А': '1',
#         'Б': '3',
#         'В': '1',
#         'Г': '3',
#         'Д': '2',
#         'Е': '1',
#         'Ё': '3',
#         'Ж': '5',
#         'З': '5',
#         'И': '1',
#         'Й': '4',
#         'К': '2',
#         'Л': '2',
#         'М': '2',
#         'Н': '1',
#         'О': '1',
#         'П': '2',
#         'Р': '1',
#         'С': '1',
#         'Т': '1',
#         'У': '2',
#         'Ф': '10',
#         'Х': '5',
#         'Ц': '5',
#         'Ч': '5',
#         'Ш': '8',
#         'Щ': '10',
#         'Ъ': '10',
#         'Ы': '4',
#         'Ь': '3',
#         'Э': '8',
#         'Ю': '8',
#         'Я': '3',
#     }
#     if len(word)==0:
#         return 'pusto'
#     word = word.upper()
#     summa = 0
#     for i in range(len(word)):
#         if word[i] in da_kakoi_blin_slovar:
#             summa+=int(da_kakoi_blin_slovar[word[i]])
#     return summa

# if __name__ == "__main__":
#     print("ПРИВЕТ (корректный):", calculate_scrabble_score("ПРИВЕТ"))
#     print("ПИТОН (корректный):", calculate_scrabble_score("ПИТОН"))
#     print("ПРОГРАММИРОВАНИЕ (корректный):", calculate_scrabble_score("ПРОГРАММИРОВАНИЕ"))
#     print("КОД (корректный):", calculate_scrabble_score("КОД"))
#     print("СИЛА (корректный):", calculate_scrabble_score("СИЛА"))
#     print(" (пустая строка):", calculate_scrabble_score(""))
#     print("привет (нижний регистр):", calculate_scrabble_score("привет"))
#     print("ПиТоН (смешанный регистр):", calculate_scrabble_score("ПиТоН"))
#     print("Hello (английские буквы):", calculate_scrabble_score("Hello"))
#     print("123 (цифры):", calculate_scrabble_score("123"))
#     print("Привет! (с восклицательным знаком):", calculate_scrabble_score("Привет!"))
#     print("ПРИ-ВЕТ (с дефисом):", calculate_scrabble_score("ПРИ-ВЕТ"))
#     print("ПРИВЕТ, МИР (с запятой и пробелом):", calculate_scrabble_score("ПРИВЕТ, МИР"))

# emails = {
# 'gryffindor.com': ['andrei_serov', 'alexander_pushkin', 'elena_belova'],
# 'hufflepuff.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
# 'hogwarts.com': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
# 'slytherin.com': ['ekaterina_ivanova', 'glebova_nastya'],
# 'ravenclaw.com': ['john.doe', 'mark.zuckerberg', 'helen_hunt']
# }

# if __name__ == '__main__':
#     for domen in emails:
#         for email in emails[domen]:
#             print(email+'@'+domen)

# Лабораторная работа 8
# Задание H: Анализ продаж магазина

# def sales_summary(price_list, sales):
#     """
#     Анализирует продажи магазина и возвращает сводку

#     Параметры:
#         price_list (dict): словарь с ценами товаров
#         sales (list): список продаж в формате (товар, количество)

#     Возвращает:
#         dict: сводка с общей выручкой, проданными товарами и топ-товаром
#     """
#     prodano = {'deneg_srubleno' : 0}
#     for tovar in sales:
#         if tovar[0] in price_list and tovar[0] not in prodano:
#             prodano[tovar[0]] = tovar[1]
#             prodano["deneg_srubleno"]+=tovar[1]*price_list[tovar[0]]
#         elif tovar[0] in price_list and tovar[0] in prodano:
#             prodano[tovar[0]]+=tovar[1]
#     if prodano["deneg_srubleno"]==0:
#         return """
#         "total_revenue": 0,
#         "items_sold": {},
#         "top_item": None"""
#     max_kol, max_tovar = 0, ''
#     for i in prodano:
#         if prodano[i]>max_kol and i!='deneg_srubleno':
#             max_kol = prodano[i]
#             max_tovar = i
#     prodano['TOP_PRODAJ'] = max_tovar
#     return prodano

# if __name__ == "__main__":
#     price_list = {"Хлеб": 50, "Молоко": 80, "Сыр": 200}
#     sales = [("Хлеб", 3), ("Молоко", 2), ("Хлеб", 1), ("Кофе", 5)]
#     result = sales_summary(price_list, sales)
#     print("Тест 1:")
#     print(result)

#     # Тест 2: Только неизвестные товары
#     price_list2 = {"Хлеб": 50, "Молоко": 80}
#     sales2 = [("Чай", 2), ("Кофе", 3)]
#     result2 = sales_summary(price_list2, sales2)
#     print("\nТест 2 (только неизвестные товары):")
#     print(result2)

#     # Тест 3: Нет продаж
#     price_list3 = {"Хлеб": 50, "Молоко": 80}
#     sales3 = []
#     result3 = sales_summary(price_list3, sales3)
#     print("\nТест 3 (нет продаж):")
#     print(result3)

#     # Тест 4: Несколько товаров с одинаковым количеством продаж
#     price_list4 = {"Хлеб": 50, "Молоко": 80, "Сыр": 200}
#     sales4 = [("Хлеб", 2), ("Молоко", 2), ("Сыр", 1)]
#     result4 = sales_summary(price_list4, sales4)
#     print("\nТест 4 (одинаковое количество продаж):")
#     print(result4)