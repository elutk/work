#имя проекта: work
#номер версии: 1.0
#имя файла: 58.py
#автор и его учебная группа: Е. Уткина, ЭУ-120
#дата создания: 27.12.2019
#дата последней модификации: 27.12.2019
#описание: Задана строка символов, в которой встречается символ «.». Поставить после каждого такого символа системное время ПК.
#версия Python: 3.8
from datetime import datetime
M = 3

list_strings = []
for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

now = str(datetime.now())

for string in list_strings:
    print(string.replace('.', '.' + now))