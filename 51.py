#имя проекта: work
#номер версии: 1.0
#имя файла: 51.py
#автор и его учебная группа: Е. Уткина, ЭУ-120
#дата создания: 26.12.2019
#дата последней модификации: 26.12.2019
#описание: Заданы M строк символов, которые вводятся с клавиатуры. Найти количество символов в самой длинной строке. Выровнять строки по самой длинной строке, поставив перед каждой строкой соответствующее количество звёздочек.
#версия Python: 3.8
A = [A * 3 for A in 'abc']
print(A)
B = ['Hello', 'world!', 'qwe']
print(B)
list.sort(B, key=len)
print(B)

for i in range(len(B)):
    if len(B[i]) < len(B[i+1]):
        list.insert(0, '*')
        i = i + 1
        
print(B)
