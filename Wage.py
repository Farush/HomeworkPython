from sys import argv

def arg_check(args=[], n=1):
    """Проверяет список с первого по n-ный индекс. Игнорирует нулевой.
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

if len(argv) > 1:

    if arg_check(argv, 3):

        if len(argv) < 3:
            print('Недостаточно данных.')

        elif len(argv) == 3:
            hours, wage_hours = argv[1:3]
            hours = int(hours)
            wage_hours = int(wage_hours)

            salary = hours * wage_hours
            print(salary)

        elif len(argv) == 4:
            hours, wage_hours, bonus = argv[1:4]
            hours = int(hours)
            wage_hours = int(wage_hours)
            bonus = int(bonus)

            salary = hours * wage_hours + bonus
            print(salary)

    else:
        print('Попробуйте запустить программу еще раз. Проверьте правильность ввода аргументов.')

else:
    print('Введите аргументы: выработка, ставка в час, премия (необязательно) ')
