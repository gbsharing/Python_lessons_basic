# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

eqPos = equation.find("=")
xPos = equation.find("x")
k = float(equation[eqPos + 1:xPos].replace(' ', ''))
b = float(equation[xPos + 1:].replace(' ', ''))
print(f"Координата y = {k*x + b} для точки с координатой x = {x}")
print(f"Выражение: {equation}")
input("Конец первой задачи\n")

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

from datetime import datetime
dateString = input("Введите дату в формате 'dd.mm.yyyy': ")
isInFormat = True
for index, symbol in enumerate(dateString):
    if (index == 2) or (index == 5):
        if symbol != ".":
            isInFormat = False
            break
    else:
        if not symbol.isdigit():
            isInFormat = False
            break
if isInFormat:
    try:
        datetime.strptime(dateString, "%d.%m.%Y")
    except Exception as e:
        print(e)
        pass
    else:
        print("Дата корректна")
else:
    print("Длина исходной строки для частей должна быть в соответствии с форматом: 2 цифры для дня, 2 - для месяца, 4 - для года")
input("Конец второй задачи\n")

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

N = int(input("Вход: "))
floor = 1 # Текущий этаж
maxCount = 1 # Максимальное количество комнат на этаже (количество этажей с одинаковым количеством комнат)
roomCount = 1 # Текущая комната по порядку

# Пропускаем блоки этажей с одинаковым количеством квартир
while roomCount < N:
    maxCount += 1
    roomCount += maxCount**2

floor = int(maxCount * (maxCount - 1) / 2) # Переходим на верхний этаж последнего блока
roomCount -= maxCount**2 # Отсчитываем последнюю комнату последнего блока
maxCount -= 1
floorCount = maxCount # Порядковый номер этажа в блоке
numInFloor = maxCount # Порядковый номер квартиры на последнем этаже последнего блока
for i in range(roomCount - 1, N - 1):
    if numInFloor == maxCount:
        if floorCount == maxCount:
            maxCount += 1
            floorCount = 1
            numInFloor = 1
            floor += 1
        else:
            floorCount += 1
            numInFloor = 1
            floor += 1
    else:
        numInFloor += 1
print(f"Выход: {floor} {numInFloor}")
input("Конец третьей задачи\nВсего доброго!")
