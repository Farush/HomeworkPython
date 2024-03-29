from random import randint
import json

# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open('text.txt', 'a') as f: # должно быть 'w', если создаем файл с нуля, но я оставил 'a'. чтоб при многократном прогоне не создавать его заново.
    line = input()
    while line:
        f.write(line+'\n')
        line = input()


# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.
# Возьмем файл, который был создан в предыдущей задаче.

line = ' '
line_number = 0
words = []

with open('text.txt', 'r') as f:
    while line: # можно while line != \n, тогда не будет считать последнюю пустую строку

        line = f.readline()
        line_number += 1
        words = line.split()
        len_words = len(words)
        print(f'В строке {line_number} количество слов: {len_words}')

    print(f'Всего строк {line_number}')

# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

with open('salary.txt', 'r') as f:
    #line = ' '
    salary_dict = {}
    line = f.readline()
    while line: # создаем словарь, ключ - имя, значение - зарплата
        info = line.split()
        name, salary = info[0], float(info[1])
        salary_dict[name] = salary
        line = f.readline()
# print(salary_dict)

average = 0
i = 0
print('Список сотрудников, которые получают меньше 20000:')
for key, val in salary_dict.items():
    average = average + val
    i += 1
    if val < 20000:
        print(key)

print(f'Средний заработок равен {round(average/i, 2)}')

# 4. Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

en_ru = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

new_lines = []

with open('numbers.txt', 'r') as f:
    lines = f.read()
    line = lines.splitlines()

    for words in line: # вылетает, если в файле есть пустые строки.
        split_words = words.split()
        #print(split_words)

        for key, val in en_ru.items():

            for i in range(len(split_words)):# так более универсально,
                                            # если не знаем на каком месте стоит слово
                if key == split_words[i]:
                    split_words[i] = val

            #if key == split_words[0]: # так если знаем, что слово точно стоит на первом месте.
            #    split_words[0] = val

        new_word = ' '.join(split_words)
        new_lines.append(new_word + '\n')

with open('ru_numbers.txt', 'w') as f:
    f.writelines(new_lines)


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('random_numbers.txt', 'w') as f:
    line = ''
    for _ in range(randint(1, 100)): # пусть будет случайное количество чисел
        line = line + str(randint(1, 10000)) + ' '
    f.write(line)

sum_of_nums = 0
with open('random_numbers.txt', 'r') as f:
    list_of_numbers = f.readline().split()

for item in list_of_numbers:
    sum_of_nums = sum_of_nums + int(item)

print(f'Сумма случайных чисел из файла: {sum_of_nums}')

# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и
# наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество
# занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести его на экран.

def cyrillic(symbol):
    """Возвращет символ кириллицы или пробел, если аргумент символ кириллицы или пробел;
    или пустоту, если символ не кириллический"""
    if 1039 < ord(symbol) < 1104 or ord(symbol) == 1025 or ord(symbol) == 1105 or ord(symbol) == 32:
        return symbol
    else:
        return ''

def digit_till_symbol(string):
        """Возвращает целое число из строки, пробегая строчку пока не наткнется на нецифру
        или ноль, если в строке нет цифр"""
        new_string = ''
        for sym in string:
            if sym.isdigit():
                new_string = new_string + sym
            else:
                if new_string.isdigit():
                    return int(new_string)
                else:
                    return 0


# print(digit_till_symbol('452(l45)'))


words = []
key = ''
hours = 0

with open('subjects.txt', 'r') as f:

    subjects = {}
    # f.seek(0, 0)
    line = f.readline() # прочитываем первую строчку из файла

    while line: # если строчка не пустая

        words = line.split() # разбиваем строку, пишем список
        # print(words)
        key = words.pop(0) # убираем первый элемент, записываем его в ключ
        key = ''.join(list(map(cyrillic, key))) # пересобираем ключ, выкидывая посторонние символы

        for word in words:
            hours = hours + digit_till_symbol(word)
        # print(hours)
        subjects[key] = hours # пишем ключ: значение в словарь
        hours = 0 # обнуляем часы, чуть не забыл )
        line = f.readline() # читаем следущую строчку из файла


print(subjects)

# 7
info_dict = {}
average = 0
with open('firms.txt', 'r') as f:
    line = f.readline()
    i = 0
    while line:
        info = line.split()
        #print(info)
        income = int(info[2]) - int(info[3])
        info_dict[info[0]] = income
        if income > 0:
            average = average + income
            i += 1
        line = f.readline()

average = round(average/i, 2)
average_profit = {'average_profit': average}
profit_list = [info_dict, average_profit]

with open('profit.json', 'w') as f:
   f.writelines(json.dumps(profit_list))
