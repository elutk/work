#имя проекта: work
#номер версии: 1.0
#имя файла: 55.py
#автор и его учебная группа: Е. Уткина, ЭУ-120
#дата создания: 27.12.2019
#дата последней модификации: 27.12.2019
#описание: Заданы M строк слов, которые вводятся с клавиатуры (в каждой строке – одно слово). Вводится слог (последовательность букв). Удалить данный слог из каждой строки.
#версия Python: 3.8
import re
M = 3
list_strings = []

for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())
print("Введите слог:", end=' ')
syllable = input()

for string in list_strings:
    string = re.sub(syllable, '', string)
    print(string)