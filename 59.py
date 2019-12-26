#имя проекта: work
#номер версии: 1.0
#имя файла: 59.py
#автор и его учебная группа: Е. Уткина, ЭУ-120
#дата создания: 27.12.2019
#дата последней модификации: 27.12.2019
#описание: Заданы M строк, которые вводятся с клавиатуры. Подсчитать количество пробелов в каждой из строк.
#версия Python: 3.8
import re
M = 3

list_strings = []
for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

for string in list_strings:
    count_spaces = len(re.findall(r'\s', string))
    print("В строке \"%s\" %s пробелов" % (string, count_spaces))