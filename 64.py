#имя проекта: work
#номер версии: 1.0
#имя файла: 64.py
#автор и его учебная группа: Е. Уткина, ЭУ-120
#дата создания: 27.12.2019
#дата последней модификации: 27.12.2019
#описание: Суммировать вводимые числа, среди которых нет нулевых. При вводе нуля обеспечить вывод текущего значения суммы. При вводе числа 99999 закончить работу.
#версия Python: 3.8
import re

list_numbers = []

sum = 0


while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)
    list_numbers.append(number)

    if number == 99999:
        break
    elif number == 0:
        print("Сумма:", sum)
    else:
        sum += number

print("Сумма:", sum)
