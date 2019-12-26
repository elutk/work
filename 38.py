# имя проекта: work
# номер версии: 1.0
# имя файла: 38.py
# автор и его учебная группа: Е. Уткина, ЭУ-120
# дата создания: 26.11.2019
# дата последней модификации: 26.12.2019
# описание: Дан одномерный массив числовых значений, насчитывающий N элементов.Исключить из него M элементов, начиная с позиции K.
# версия Python: 3.8
import numpy as np
import array
import random

N = int(input("Введите количество элементов массива "))
K = int(input("Позиция K "))
M = int(input("количество элементов для вычитания "))
A = [random.randint(0, 100) for i in range(0, N)]
print(A)

A.insert(K,M)
print(A)

A.delete(K,M)