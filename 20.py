import math
x = int(input("Введите число для проверки:"))
a = int(input("Укажите начало промежутка:"))
b = int(input("Укажите конец промежутка:"))

if math.fabs(a) <= math.fabs(x) <= math.fabs(b):
    print("Число ",x, " Принадлежит множеству [",a,",",b,"]")
else:
    print("Число ",x, " не принадлежит множеству [",a,",",b,"]")