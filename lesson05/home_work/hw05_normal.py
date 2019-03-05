# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import hw05_easy, sys, os

file_path = os.getcwd()

def print_help():
    print("help - Получение справки")
    print("cd - Перейти в папку")
    print("lof - Просмотреть содержимое текущей папки")
    print("df - Удалить папку")
    print("cf - Создать папку")

def change_dir():
    name = input("Напишите название папки для перехода (пустая строка для перехода в начальную папку): ")
    if name == "":
        os.chdir(file_path)
        print("Вы в начальной папке: ", file_path)
    else:
        dir_path = os.path.join(os.getcwd(), name)
        try:
            os.chdir(dir_path)
            print("Успешно перешел")
        except:
            print("Невозможно перейти")

def list_of_folder():
    print(os.listdir(os.getcwd()))

def delete_dir():
    name = input("Напишите название папки для удаления: ")
    hw05_easy.delete_folder(name)

def create_dir():
    name = input("Напишите название папки для создания: ")
    hw05_easy.create_folder(name)

do = {
    "help": print_help,
    "cd": change_dir,
    "lof": list_of_folder,
    "df": delete_dir,
    "cf": create_dir
}

while True:
    key = input("\nНапишите ключ действия или 'q' для выхода:\n")

    if key == 'q':
        sys.exit()
    else:
        if do.get(key):
            do[key]()
        else:
            print("Задан неверный ключ")
            print("Укажите ключ help для получения справки")
