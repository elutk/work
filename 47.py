# имя проекта: work
# номер версии: 1.0
# имя файла: 47.py
# автор и его учебная группа: Е. Уткина, ЭУ-120
# дата создания: 26.11.2019
# дата последней модификации: 26.12.2019
# описание: Дан одномерный массив числовых значений, насчитывающий N элементов. Исключить из массива элементы, принадлежащие промежутку [B; C].
# версия Python: 3.8
import random
import numpy
N = int(input("Количество элементов массива"))
B = int(input("Элемент массива 1"))
C = int(input("Элемент массива 2"))
A = [random.randint(-10, 10) for i in range(0, N)]
print(A)
C = C + 1
del A[B:C]
print(A)