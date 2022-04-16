import math
from itertools import count
from sys import argv
from math import factorial

def arg_check(args=[], n=1):
    """Проверяет список с первого по n-ный индекс. Игнорирует нулевой индекс.
    Если все эти элементы цифры, возвращает True, в противном случае False и выводит эелементы,
    которые не являются цифрами"""

    for arg in args[1:n+1]:
        if not arg.isdigit():
            print(f'Аргументы должны быть численные. Аргумент "{arg}" не является числом')
            flag = False
            #break если так, то напечатает только первый неверный аргумент. Уберем. Пусть напечатает все.
        else:
            flag = True
    return flag

def fact(n):
    # без использования модуля math не могу придумать, как написать объект-генератор
    #number = 1
    #for i in range(1, n + 1):
        #number *= i
        #yield number

    f = (factorial(i) for i in range(1, n+1)) # объект генератор, но с использованием модуля math
    for number in f:
        yield number
if len(argv) > 1:

    if arg_check(argv, 1):

        f = fact(int(argv[1]))
        for number in f:
            print(number)
    else:
        print('Введите целое положительное число.')

else:
    print('Введите аргумент.')