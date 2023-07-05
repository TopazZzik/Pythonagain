#Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# import os

# def get_file_path(path):
#     """
#     Функция принимает на вход абсолютный путь до файла и возвращает кортеж из трех элементов: путь,
#     имя файла и расширение файла. Если файл не найден, возвращается None.
#     :param path: абсолютный путь до файла
#     :return: кортеж из пути, имени и расширения файла
#     """

#     # Проверяем, что путь существует
#     if not os.path.exists(path):
#         return None

#     path, filename = os.path.split(path)
#     extension = os.path.splitext(filename)[1]

#     return path, filename, extension

# # Пример использования
# path = "C:/Users/user/Desktop/file.txt"
# path_name, file_name, extension = get_file_path(path)
# print(path_name) # C:/Users/user/Desktop
# print(file_name)  # file.txt
# print(extension)  # .txt

# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида «10.25%». 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии
# d = {}
# for name, rate, percent in zip(names, rates, premiums):
#     d[name] = (rate * 100) * ((1 + float(percent)) / 100)

#Создайте функцию генератор чисел Фибоначчи

def fib_generator():
    current, next_num = 0, 1

    while True:
        yield current
        current, next_num = next_num, current + next_num

fibo_seq = fib_generator()

for i in range(30):
    print(fibo_seq.__next__())



