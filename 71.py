#имя проекта: work
#номер версии: 1.0
#имя файла: 71.py
#автор и его учебная группа: Е. Уткина, ЭУ-120
#дата создания: 27.12.2019
#дата последней модификации: 27.12.2019
#описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Определить средние значения по всем строкам и столбцам матрицы. Результат оформить в виде матрицы из N + 1 строк и M + 1 столбцов.
#версия Python: 3.8
import random

N = 4
M = 5


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


def get_average(row):
    sum = 0
    for element in row:
        sum += element

    return sum/len(row)


def get_column(matrix, index):
    column = []
    i = 0
    while i < len(matrix):
        column.append(matrix[i][index])
        i += 1

    return column


A = get_matrix(N, M)
print("Исходная матрица:")
print_matrix(A)


for row in A:
    average = get_average(row)
    row.append(average)


i = 0
new_row = []
while i < len(A[0]):
    column = get_column(A, i)
    average = get_average(column)
    new_row.append(average)
    i += 1

print("Модифицированная матрица:")
A.append(new_row)

print_matrix(A)