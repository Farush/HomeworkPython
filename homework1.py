
# 1. Раздел с переменными

a = 2345
b = '2345'

print(type(a))
print(a)
print(type(b))
print(b)

#c = input("Введите число: ")
#if c.isdigit():
#    print('you entered number ', c)
#else:
#    print(c, ' is not a number')

while True:
    c = input("Введите число: ")
    if c.isdigit():
        print(type(c))
        print('you entered number ', c)
        break
    else:
        print(c, ' is not a number')


while True:
    c = input("Введите строку: ")
    if not c.isdigit():
        print('you entered string ', c)
        break
    else:
        print(c, ' is a string but contains digits')


# 2.Раздел с секундами, которые мы переводим в часы и минуты

while True:
    seconds = input("Введите количество секунд: ")
    if seconds.isdigit() and int(number) >= 0
        seconds = int(seconds)
        break
    else:
        print("Вы ввели неверные данные, должно быть целое положительное число. ")

hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60

print(f'{hours}:{minutes}:{seconds}')

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
while True:
    digit = input("Введите число от одного до девяти: ")
    if digit.isdigit() and len(digit) == 1:
        digit2 = int(digit * 2)
        digit3 = int(digit * 3)
        digit = int(digit)
        break
    else:
        print("Вы ввели неверные данные, должно быть целое число одного до девяти. ")


print(digit + digit2 + digit3)


# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
while True:
    number = input("Введите целое положительное число: ")
    if number.isdigit() and not (int(number) < 0):
        i = len(number)
        number = int(number)
        break
    else:
        print('Вы ввели неверные данные. Число должно быть целым и положительным.')

print(f'В числе {number} {i} разряд(а)(ов)')
max_number = 0
while i != 0:
    i -= 1
    temp_digit = number // (10**i)
    number = number % (10**i)
    max_number = temp_digit if temp_digit > max_number else max_number
    #print(10**i, b)
print(f'Самая большая цифра это {max_number}')

#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма.
while True:
    income = input("Введите сумму выручки. Это должно быть целое положительное число: ")
    if income.isdigit() and not (int(income) < 0):
        income = int(income)
        break
    else:
        print('Вы ввели неверные данные. Число должно быть целым и положительным.')

while True:
    expences = input("Введите сумму расходов. Это должно быть целое положительное число: ")
    if expences.isdigit() and not (int(expences) < 0):
        expences = int(expences)
        break
    else:
        print('Вы ввели неверные данные. Число должно быть целым и положительным.')

fin_result = income - expences
print(f'Прибыль фирмы составила {fin_result}') if fin_result >= 0 else print(f'Убыток фирмы составил {fin_result*-1}')

#6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
if fin_result > 0:
    rentability = fin_result / income
    print(f'Рентабельность предприятия сотавила {int(round(rentability, 2) * 100)}%')

while True:
    workers = input("Введите количество работников предприятия. Это должно быть целое положительное число: ")
    if workers.isdigit() and not (int(workers) < 0):
        workers = int(workers)
        break
    else:
        print('Вы ввели неверные данные. Число должно быть целым и положительным.')

print(f'Прибыль предприятия в расчете на одного сотрудника составила {fin_result / workers}')

#7 (Дополнительно). Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего. Требуется определить номер дня,
# на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

while True:
    a = input("Введите количество километров, которое спортсмен пробежал в первый день. \nЭто должно быть целое положительное число: ")
    if a.isdigit() and not (int(a) < 0):
        a = int(a)
        break
    else:
        print('Вы ввели неверные данные. Число должно быть целым и положительным.')

while True:
    b = input("Введите количество километров, которое спортсмен должен пробежать. Мы расчитаем, в какой день это произойдет, \nесли каждый день спортсмен будет улучшать свой результат на 10% \nЭто должно быть целое положительное число: ")
    if b.isdigit() and not (int(b) < 0):
        b = int(b)
        break
    else:
        print('Вы ввели неверные данные. Число должно быть целым и положительным.')
i = 0
print('Результат:')
while a < b:
    i += 1
    print(f'{i}-й день: {round(a, 2)}')
    a = a + a/10
i += 1
print(f'{i}-й день: {round(a, 2)}')
print(f'На {i}-й день спортсмен достиг результата - не менее {b} км.')


