A = float(input("Введите вещественное число A:"))
B = float(input("Введите вещественное число B:"))
C = float(input("Введите вещественное число C:"))

if A < B and B > C:
    print("Оба неравенства выполняются:")
if A < B:
    print("Выполняется неравенство А < B:")
if B > C:
    print("Выполняется неравенство B > C:")