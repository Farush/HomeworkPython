from functools import reduce

from itertools import count, cycle

# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [old_list[i] for i in range(1, len(old_list)) if old_list[i] > old_list[i-1]]

print(new_list)

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.

list_of_numbers = [number for number in range(20, 241) if number % 21 == 0 or number % 20 == 0]

print(list_of_numbers)

# 4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
old_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

list_of_numbers = [old_list[i] for i in range(len(old_list)) if old_list.count(old_list[i]) == 1]
print(list_of_numbers)

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.

even_numbers = [number for number in range(100, 1001, 2)]

multi = lambda a, b: a * b

result = reduce(multi, even_numbers)

print(result)




