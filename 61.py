#имя проекта: work
#номер версии: 1.0
#имя файла: 61.py
#автор и его учебная группа: Е. Уткина, ЭУ-120
#дата создания: 27.12.2019
#дата последней модификации: 27.12.2019
#описание: Последовательно вводятся числа. Определить сумму чисел с нечётными номерами и произведение чисел с чётными номерами (по порядку ввода). Подсчитать количество слагаемых и количество сомножителей. При вводе числа 55555 закончить работу.
#версия Python: 3.8
import re

list_numbers = []

sum = 0
sum_count = 0

multiply = 1
multiply_sum = 0


i = 1
while True:
    print("Введите число:", end=' ')
    string = re.sub(r'\D', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)
    list_numbers.append(number)

    if i % 2 != 0:
        sum += number
        sum_count += 1
    else:
        multiply = multiply * number
        multiply_sum += 1

    i += 1
    if list_numbers[len(list_numbers) - 1] == 55555:
        break


print("Сумма:", sum)
print("Количество слагаемых:", sum_count)

print("Произведение", multiply)
print("Количество множителей:", multiply_sum)