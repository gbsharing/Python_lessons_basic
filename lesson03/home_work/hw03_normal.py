# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    n, m = int(n), int(m)
    res = []
    a = 1
    b = 1
    if 1 >= n:
        res.append(a)
    for i in list(range(1, m)):
        if i >= n - 1:
            res.append(b)
        a, b = b, (a + b)
    return res

print(fibonacci(input("Введите n-элемент: "), input("Введите m-элемент: ")))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    is_not_fine = True
    while is_not_fine:
        is_not_fine = False
        for i in list(range(len(origin_list)-1)):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
                is_not_fine = True
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def own_filter(func, iterator):
    # Работает только для списков
    res = []
    for el in iterator:
        if func(el):
            res.append(el)
    return res

dict_a = ['name', 'python', 'points', 'name', 'java', 'points']
print(own_filter(lambda x : x == 'points', dict_a))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math

def is_parallelogram(A):
    A1, A2, A3, A4 = A

    # Скалярное произведение векторов
    def scalar_mult_vect(V1, V2):
        return V1[0] * V2[0] + V1[1] * V2[1]

    # Длина вектора
    def len_vect(V):
        return math.sqrt(V[0]**2 + V[1]**2)

    # Вектор по двум точкам
    def vector(A1, A2):
        return (A2[0] - A1[0], A2[1] - A1[1])

    # Проверка, что все точки разные
    is_all_dot_uniq = True
    for i, el in enumerate(A):
        if el in A[i+1:]:
            is_all_dot_uniq = False
            break

    if is_all_dot_uniq:
        # Проверка, что A1A2 параллелен A3A4 и равен по длине
        A1A2 = vector(A1, A2)
        A3A4 = vector(A3, A4)
        if (abs(scalar_mult_vect(A1A2, A3A4)) == len_vect(A1A2)**2):
            return "Это параллелограмм - 1"
        else:
            A1A3 = vector(A1, A3)
            A2A4 = vector(A2, A4)
            if (abs(scalar_mult_vect(A1A3, A2A4)) == len_vect(A1A3)**2):
                return "Это параллелограмм - 2"
            else:
                return "Это не параллелограмм"
    else:
        return "Есть повторяющиеся точки"

x1 = int(input("Введите x1: "))
x2 = int(input("Введите x2: "))
x3 = int(input("Введите x3: "))
x4 = int(input("Введите x4: "))
y1 = int(input("Введите y1: "))
y2 = int(input("Введите y2: "))
y3 = int(input("Введите y3: "))
y4 = int(input("Введите y4: "))

##x1 = 0
##x2 = 1
##x3 = 0
##x4 = 1
##y1 = 0
##y2 = 2
##y3 = 1
##y4 = 10

print(is_parallelogram([(x1, y1), (x2, y2), (x3, y3), (x4, y4)]))
