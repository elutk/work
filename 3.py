#имя проекта: work
#номер версии: 1.0
#имя файла: 3.py
#автор и его учебная группа: Е. Уткина, ЭУ-120
#дата создания: 05.11.2019
#дата последней модификации: 26.12.2019
#описание: Известны длины трёх сторон треугольника. Вычислить периметр треугольника и площадь по формуле Герона (указание: использовать модуль math и функцию sqrt ()).
#версия Python: 3.8
import math

a = 3
b = 5
c = 7
p = (a + b + c) / 2
print (p * 2)
S = math.sqrt ( p * (p - a) * ( p - b) * ( p - c))
print (S)
