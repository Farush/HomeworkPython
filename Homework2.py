# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.

my_list = [2, 'qwerty', [12, 'apple'], None, False]

for item in my_list:
    print(type(item))

# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.

some_string = input('Введите список элементов через пробел: ')
some_list = some_string.split(' ')

print(some_list)

for i in range(len(some_list) // 2):
    # print(some_list[i * 2])
    some_list[i * 2], some_list[i * 2 + 1] = some_list[i * 2 + 1], some_list[i * 2]

print(some_list)

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

some_string = input('Введите несколько слов, разделенных пробелом: ')

some_list = some_string.split(' ')
i = 0
for word in some_list:
    i += 1
    print(f'{i}. {word[:10]}')

# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.


rating_list = [7, 5, 3, 3, 2]

while True:
    rating = input("Введите рейтинг: ")
    if rating.isdigit():
        rating = int(rating)
        break
    else:
        print("Вы ввели неверные данные, должно быть целое положительное число. ")
i = 0

for i in range(len(rating_list)):
    if rating_list[i] < rating:
        rating_list.insert(i, rating)
        break
    else:
        i += 1

if i == len(rating_list):  # если не находим в списке числа, которое меньше нашего
    rating_list.append(rating)

print(rating_list)

# или просто запихиваем в конец, сортируем и разворачиваем.
# rating_list.append(rating)
# rating_list.sort()
# rating_list.reverse()
# print(rating_list)

# 6. (Дополнительно) Реализовать структуру данных «Товары».
goods = []
i = 0
while True:

    name = input('Введите наименование товара: ')

    while True:
        price = input('Введите цену товара: ')
        if price.isdigit():
            price = int(price)
            break
        else:
            print('неверно, повторите ввод. Должно быть число.')
            continue

    while True:
        amount = input('Введите количество товара: ')
        if amount.isdigit():
            amount = int(amount)
            break
        else:
            print('неверно, повторите ввод. Должно быть число.')
            continue

    units = input('Введите единицу измерения количества товара: ')

    answer = input(f'Проверьте правильность введенных  данных. \nНаименование: {name}, \nцена: {price}, '
                   f'\nколичество: {amount}, \nединицы измерения: {units} \n'
                   f'Все верно? y/n (д/н)?: ')

    if answer.lower() == 'y' or answer.lower() == 'д':
        i += 1
        goods.append((i, {'наименование': name, 'цена': price, 'количество': amount, 'ед.': units}))
        # print(goods)
    else:
        print('Еще раз внимательно введите данные о товаре.')
        continue

    answer = input(f'Продожить ввод товаров?" y/n (д/н)?: ')
    if answer.lower() == 'y' or answer.lower() == 'д':
        continue
    else:
        break

# Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.

# goods = [
#    (1, {'наименование': 'vodka', 'цена': 456, 'количество': 56, 'ед.': 'bottle'}),
#    (2, {'наименование': 'beer', 'цена': 45, 'количество': 789, 'ед.': 'bottle'}),
#    (3, {'наименование': 'wine', 'цена': 405, 'количество': 1789, 'ед.': 'bottle'})
# ]


analitics_dict = {}

for key in goods[1][1].keys():
    # print(key)
    i = 0
    item_list = []
    for item in goods:  # по идее надо key in goods[i][1] или нет? но так все равно работает.
        item_list.append(goods[i][1].get(key))
        #if goods[i][1].get(key) not in item_list:
            #item_list.append(goods[i][1].get(key))  # будет игнорить item, если он уже есть в списке. Надо ли?
            # если в списке будут два одинаковых наименования или цены? В задании не указано.
        i += 1
    #analitics_dict[key] = item_list так, если игнорим повторяющиеся items при составлении словаря

    if key != 'ед.': # так, если позволяем собрать словарь с повторениями,
        # но нужно, чтоб единицы измерения не повторялись.
        analitics_dict[key] = item_list
    else:
        analitics_dict[key] = list(set(item_list))
    # print(item_list)
print(analitics_dict)
