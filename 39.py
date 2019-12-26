# имя проекта: work
# номер версии: 1.0
# имя файла: 39.py
# автор и его учебная группа: Е. Уткина, ЭУ-120
# дата создания: 26.11.2019
# дата последней модификации: 26.12.2019
# описание: Дан одномерный массив числовых значений, насчитывающий N элементов. Исключить все нулевые элементы.
# версия Python: 3.8
import random
N = int(input("Введите количество элементов массива "))
A = [random.randint(-1, 1) for i in range(0, N)]
print(A)
B = filter(bool, A)
print(list(B))