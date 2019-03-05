import os

def create_folder(name):
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print("Успешно создано")
    except:
        print("Невозможно создать")

def list_of_folders():
    file_path = os.getcwd()
    dirs = []
    for r, d, f in os.walk(file_path):
        if r == file_path:
            dirs = d
    return dirs

def delete_folder(name):
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.removedirs(dir_path)
        print("Успешно удалено")
    except:
        print("Невозможно удалить")

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

if __name__ == "__main__":
    for i in range(1, 10):
        create_folder(f"dir_{i}")

    print("В результате получились вот что:", list_of_folders())

    input("Будем удалять... Нажмите Enter")

    for i in range(1, 10):
        delete_folder(f"dir_{i}")

    print("В результате осталось вот что:", list_of_folders())
    input()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

if __name__ == "__main__":
    print("В текущей директории следующие папки:", list_of_folders())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

if __name__ == "__main__":
    import shutil
    shutil.copy(__file__, os.path.abspath('file_copy.py'))
    print("Исполняемый файл скопирован")
