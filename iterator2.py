from itertools import cycle
from sys import argv

# 6. 10 раз печатаем список, полученный из введенных аргументов

input_list = argv[1:]
i = 0
for item in cycle(input_list):
    print(item)
    i += 1
    if i == len(input_list)*10:
        break
