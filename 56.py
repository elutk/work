#имя проекта: work
#номер версии: 1.0
#имя файла: 56.py
#автор и его учебная группа: Е. Уткина, ЭУ-120
#дата создания: 27.12.2019
#дата последней модификации: 27.12.2019
#описание: Заданы M строк символов, которые вводятся с клавиатуры. Напечатать все центральные буквы строк нечетной длины.
#версия Python: 3.8
import math
M = 3

list_strings = []
for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

for string in list_strings:
    strlen = len(string)

    if strlen % 2 != 0:
        print(string[math.ceil(strlen/2) - 1])