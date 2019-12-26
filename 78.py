#имя проекта: work
#номер версии: 1.0
#имя файла: 78.py
#автор и его учебная группа: Е. Уткина, ЭУ-120
#дата создания: 27.12.2019
#дата последней модификации: 27.12.2019
#описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Разделить элементы каждой строки на элемент этой строки с наибольшим значением.
#версия Python: 3.8
import random

N = 4
M = 5

L = 2


def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(0, 9))

    return col


def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))

    return matrix


def print_matrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        row = matrix[i]
        while j < len(row):
            column = row[j]
            print(column, end=' ')
            j += 1

        print()
        i += 1


A = get_matrix(N, M)
print("Исходная матрица:")
print_matrix(A)

i = 0
while i < len(A):
    j = 0
    max_element = max(A[i])
    while j < len(A[i]):
        A[i][j] /= max_element
        A[i][j] = round(A[i][j], 1)
        j += 1

    i += 1

print("Модифицированная матрица:")
print_matrix(A)