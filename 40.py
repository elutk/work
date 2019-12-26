# имя проекта: work
# номер версии: 1.0
# имя файла: 40.py
# автор и его учебная группа: Е. Уткина, ЭУ-120
# дата создания: 26.11.2019
# дата последней модификации: 26.12.2019
# описание: Дан одномерный массив числовых значений, насчитывающий N элементов. После каждого отрицательного элемента вставить новый элемент, равный квадрату этого отрицательного элемента.
# версия Python: 3.8
import random
N = int(input("Количество элементов массива"))
A = [random.randint(-10,10) for i in range(0, N)]
print(A)
for i in range(N):
    if A[i] < 0:
        A[i] = A[i]**2
print(A)