# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя (в функции или за ее пределами?),
# предусмотреть обработку ситуации деления на ноль.

def division(a=float, b=float):
    """ Возвращает результат деления первого аргумента на второй. При попытке ввести неверные аргументы или
    попытке поделить на ноль возвращает None"""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print('Вы пытаетесь поделить на ноль.')
    except TypeError:
        print('введены неверные аргументы.')

    return result


a, b = input('Введите два числа: ').split()
if a.isdigit() and b.isdigit():
    a = float(a)
    b = float(b)

print(division(a, b))


# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.


def userinfo(name='Name unknown', surname='Surname unknown',
             birth_year='неизвестно', city='unknown', email='unknown', phone='Unknown'):
    """ Осуществляет вывод данных о пользователе одной строкой."""

    print(f'{name} {surname} {birth_year}го года рождения. Город проживания: {city}, email: {email}, номер телефона: {phone}')
    # это если печатаем прямо из функции

    #info = (f'{name} {surname} {birth_year}го года рождения. Город проживания: {city}, email: {email}, номер телефона: {phone}')
    #return info   Это если передаем строку из функции

userinfo(name='Вася', surname='Пупкин', birth_year=1978, city='Саранск', email='vasya@saranska.net', phone='+7 891 234 56 70')

#print(userinfo(name='Вася', surname='Пупкин', city='Саранск', email='vasya@saranska.net', ))

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    list = [a, b, c]
    list.sort()
    return list[1] + list[2]

print(my_func(12, 3, 6))

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).

def my_func2(x, y):
    result = None
    if y > 0:
        print('Неверный аргумент, число должно быть отрицательным')
    else:
        i = 0
        result = 1
        while i < abs(y):
            result = result * (1 / x)
            i += 1
    return result

print(my_func2(2, -3))
# print(2 ** -3)

# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

sum_of_numbers = 0
stop_sign = False

while not stop_sign:

    input_str = input('Введите числа: ')
    input_lst = input_str.split()

    for str in input_lst:
        if str.isdigit(): # игнорируем не цифры
            sum_of_numbers = sum_of_numbers + int(str)
        elif str == 'stop': # по стоп-слову (XD) включаем флаг
            stop_sign = True
            break
        else:
            continue

    print(sum_of_numbers)

# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text

def int_func(some_string):
    return some_string.capitalize()

print(int_func('маленькие_буквы'))

# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().

text = input('Введите строку: ')
words = text.split()
i = 0
for word in words:
    words[i] = int_func(word)
    i += 1
new_text = ' '.join(words)


print(new_text)
