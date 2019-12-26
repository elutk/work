# имя проекта: work
# номер версии: 1.0
# имя файла: 46.py
# автор и его учебная группа: Е. Уткина, ЭУ-120
# дата создания: 26.11.2019
# дата последней модификации: 26.12.2019
# описание: Дан одномерный массив числовых значений, насчитывающий N элементов. Дано положительное число T. Разделить это число между положительными элементами массива пропорционально значениям этих элементов и добавить полученные доли к соответствующим элементам.
# версия Python: 3.8
import random
import numpy

N = int(input("Количество элементов массива"))
T = int(input("Положительное число"))
A = [random.randint(-10, 10) for i in range(0, N)]

print(A)

S = 0
for i in range(N):
    if A[i] > 0:
        S = S + A[i]
K = T/S
for i in range(N):
    if A[i] > 0:
        A[i] += (A[i]*K)
        
print(K)
print(A)
