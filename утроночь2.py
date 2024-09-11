x = int(input("Введите любое число: "))
if 5 <= x <= 11:
    print("утро")
elif 12 <= x <= 17:
    print("DAY")
elif 18 <= x <= 22:
    print("evening")
elif 23 <= x <= 24 or 0 <= x <= 4:
    print("НоЧь")
else:
    print("Oшибка")