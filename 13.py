#имя проекта: work
#номер версии: 1.0
#имя файла: 13.py
#автор и его учебная группа: Е. Уткина, ЭУ-120
#дата создания: 05.11.2019
#дата последней модификации: 26.12.2019
#описание: Можно ли из бревна, имеющего диаметр поперечного сечения D, выпилить квадратный брус шириной A?
#версия Python: 3.8
import math
D = int(input("Введите диаметр поперечного сечения:"))
A = int(input("Введите ширину квадратного бруса:"))
A = math.sqrt(2) * A
print("Диагональ бруса равна",A)
if (A <=D):
    print("Выпилить квадратный брус шириной ",A,"возможно")
else:
    print("Выпилить квадратный брус шириной ", A, "невозможно")
