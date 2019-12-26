#имя проекта: work
#номер версии: 1.0
#имя файла: 20.py
#автор и его учебная группа: Е. Уткина, ЭУ-120
#дата создания: 06.11.2019
#дата последней модификации: 26.12.2019
#описание: Дано число X. Определить, принадлежит ли это число заданному промежутку [a,b].
#версия Python: 3.8
import math
x = int(input("Введите число для проверки:"))
a = int(input("Укажите начало промежутка:"))
b = int(input("Укажите конец промежутка:"))

if math.fabs(a) <= math.fabs(x) <= math.fabs(b):
    print("Число ",x, " Принадлежит множеству [",a,",",b,"]")
else:
    print("Число ",x, " не принадлежит множеству [",a,",",b,"]")
