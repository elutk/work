v = int(input("Скорость автомобиля:"))
t = int(input("Температура на улице:"))
if (v > 80 and t<=0) or (v > 60 and t <= -10):
    print("Езжай аккуратнее, гололед")
    v = v / 2
    print("Рекомендуемая скорость езды:", v)
elif (v > 120 and t>=30) or (v > 100 and t >= 45):
    print("Едь медленее, машина может заглохнуть")
    v = v / 3
    print("Рекомендуемая скорость езды:", v)
else:
    print("Условия для езды нормальные, едь как хочешь")