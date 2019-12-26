# имя проекта: work
# номер версии: 1.0
# имя файла: 44.py
# автор и его учебная группа: Е. Уткина, ЭУ-120
# дата создания: 26.11.2019
# дата последней модификации: 26.12.2019
# описание: Дан одномерный массив числовых значений, насчитывающий N элементов. Добавить столько элементов, чтобы элементов с положительными и отрицательными значениями стало бы поровну.
# версия Python: 3.8
import random
import numpy as np
N = int(input("Количество элементов массива"))
A = [random.randint(-10,10) for i in range(0,N)]
print(A)
Ao = []
Ap = []
for i in range(N):
    if A[i] > 0:
        Ap.append(A[i])
    if A[i] < 0:
        Ao.append(A[i])
sumAo = np.size(Ao)
sumAp = np.size(Ap)
Q = sumAo-sumAp
W = sumAp - sumAo
print(sumAo)
print(sumAp)
if sumAo == sumAp:
    print("Количество отрицательных и положительных элементов массива равно")
if sumAo > sumAp:
    A.append([random.randint(1,10) for i in range(0,Q)])
if sumAp > sumAo:
    A.append([random.randint(-1, -10) for i in range(0,W)])
print(A)