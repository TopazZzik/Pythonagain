# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


# def double_list(array: list[int]) -> list[int]:
#     res = set()
#     for el in array:
#         counter = array.count(el)
#         if counter > 1:
#             res.add(el)
#     return list(res)


# print(double_list([2, 2, 3, 3, 4]))



# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

# def most_frequent(text: str) -> list[str]:
#     dict_counts = {}
#     SHOW_LIMIT = 10
#     new_sorted_dictionary = {}
#     new_text = text.replace(',', ''). \
#         replace('.', ''). \
#         replace('!', ''). \
#         replace('?', ''). \
#         replace('"', ''). \
#         lower(). \
#         strip()
#     words_list = new_text.split()
#     for word in words_list:
#         counter = words_list.count(word)
#         dict_counts[word] = counter
#     sorted_values = sorted(dict_counts.values())[::-1]
#     for i in sorted_values:
#         for k in dict_counts.keys():
#             if dict_counts[k] == i:
#                 new_sorted_dictionary[k] = dict_counts[k]
#     return list(new_sorted_dictionary.items())[0: SHOW_LIMIT]

# text = 'Python — это язык программирования, который широко используется в интернет-приложениях, \
#     разработке программного обеспечения, науке о данных и машинном обучении (ML). \
#         Разработчики используют Python, потому что он эффективен, прост в изучении и работает на разных платформах. \
#             Программы на языке Python можно скачать бесплатно, они совместимы со всеми типами систем и повышают скорость разработки.'

# print(most_frequent(text))


# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

# stuff = {'matches': 1, 'cup': 2, 'tent': 10, 'ration': 5, 'spare shoes': 3}

# def backpack_capacity(capacity: int, stuff: dict) -> list[str]:
#     packaging_option = []
#     summary = []
#     for key, value in stuff.items():
#         if value <= capacity:
#             capacity -= value
#             packaging_option.append(key)
#     return packaging_option


# print(backpack_capacity(15, stuff))