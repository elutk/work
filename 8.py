#имя проекта: work
#номер версии: 1.0
#имя файла: 8.py
#автор и его учебная группа: Е. Уткина, ЭУ-120
#дата создания: 05.11.2019
#дата последней модификации: 26.12.2019
#описание: Дано натуральное число. Определить, будет ли это число: нечётным, кратным 5.
#версия Python: 3.8
num = int(input("Введите число для проверки:"))
if num % 2 == 1 and num % 5 == 0:
    print("Число", num, "нечетно и кратно 5")
else:
    print("Число не соответсвует условию")
