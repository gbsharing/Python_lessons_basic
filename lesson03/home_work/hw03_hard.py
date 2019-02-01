# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

import math

# Ищем компоненты дроби и расскладываем их по словарю
def read_fraction(str_fraction):
    int_with_fraction = str_fraction
    fraction = {"sign": 1, "int": 0, "num": 0, "den": 1}
    
    # Находим минус
    if str_fraction[0] == "-":
        fraction["sign"] *= -1
        int_with_fraction = str_fraction[1:]

    # Находим знак деления
    if "/" in int_with_fraction:
        # Всё, что после знака деления - делитель
        fraction["den"] = int(int_with_fraction[int_with_fraction.find("/") + 1:])
        int_with_num = int_with_fraction[:int_with_fraction.find("/")]

        # Если есть пробел в оставшейся части, значит есть целая часть
        if " " in int_with_num:
            fraction["int"], fraction["num"] = [int(item) for item in int_with_num.split(" ")]
        else:
            fraction["num"] = int(int_with_num)

    # Если знака "/" нет, значит всё число целое
    else:
        fraction["int"] = int(int_with_fraction)
    return fraction

# Выводим 
def write_fraction(fraction):
    return "-" * (fraction["sign"]==-1) + (str(fraction["int"]) + " " * (fraction["den"]!=1)) * (fraction["int"]!=0) + \
           (str(fraction["num"]) + "/" + str(fraction["den"])) * (fraction["den"]!=1)

#expression = input("Введите выражение: ")
expression = "5/6 + 4/7"
f_result = {"sign": 1, "int": 0, "num": 0, "den": 1}
str_f_1 = str_f_2 = ""
position = 0

if (" + " in expression) or (" - " in expression):
    if " - " in expression:
        position = expression.find(" - ")
    else:
        position = expression.find(" + ")

    str_f_1 = expression[:position]
    str_f_2 = expression[position + 3:]
    f_1 = read_fraction(str_f_1)
    f_2 = read_fraction(str_f_2)

    if " - " in expression:
        f_2["sign"] *= -1

    if (f_1["den"] == 0) or (f_2["den"] == 0):
        print("На ноль делить нельзя!")
    else:
        num_result = f_1["sign"]*(f_1["int"]*f_1["den"] + f_1["num"])*f_2["den"] + \
                     f_2["sign"]*(f_2["int"]*f_2["den"] + f_2["num"])*f_1["den"]
        f_result["den"] = f_1["den"] * f_2["den"]
        f_result["sign"] = 1
        if num_result < 0:
            num_result *= -1
            f_result["sign"] *= -1
        f_result["int"], f_result["num"] = divmod(num_result, f_result["den"])

        # Находим наибольший общий делитель
        NOD = int(math.sqrt(f_result["den"]))
        while (f_result["num"]%NOD != 0) or (f_result["den"]%NOD != 0):
            NOD -= 1

        f_result["den"] //= NOD
        f_result["num"] //= NOD
        print(write_fraction(f_result))
else:
    print("Неверный формат записи выражения. Знаки сложения и вычитания должны выделяться пробелами.")

print()

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os

DIR = "data"

workers = {}
hours_of = {}
sallary = {}

# Читаем данные из файла
with open(os.path.join(DIR, "workers"), "r", encoding="UTF-8") as f:
    is_head = True
    for line in f:
        if is_head:
            is_head = False
        else:
            worker = line.split()
            workers[worker[0] + " " + worker[1]] = [int(worker[2]), int(worker[4])]

with open(os.path.join(DIR, "hours_of"), "r", encoding="UTF-8") as f:
    is_head = True
    for line in f:
        if is_head:
            is_head = False
        else:
            hour_of = line.split()
            worker = hour_of[0] + " " + hour_of[1]
            hour = int(hour_of[2])
            hours_of[worker] = hour
            sallary[worker] = workers[worker][0] * hour / workers[worker][1] if hour < workers[worker][1] \
                              else 2 * workers[worker][0] * hour / workers[worker][1] - workers[worker][0]
            sallary[worker] = int(sallary[worker])
print("Работник: Зарплата, Норма")
print(workers)
print("\nРаботник: Часы")
print(hours_of)
print("\nРаботник: Зарплата")
print(sallary)
print()

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord("А"), ord("Я")+1))))

list_of = {}

with open(os.path.join(DIR, "fruits.txt"), "r", encoding="UTF-8") as f:
    fruits = f.read().split("\n\n")
for fruit in fruits:
    if fruit[0] in list_of.keys():
        list_of[fruit[0]].append(fruit)
    else:
        list_of[fruit[0]] = [fruit]

for char in list_of:
    with open(os.path.join(DIR, "fruits_" + char + ".txt"), "w", encoding="UTF-8") as f:
        f.write("\n".join(list_of[char]))

    
