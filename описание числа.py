x = int(input("Введите любое число: "))
if x == 0:
    print("Ноль")
elif x > 0:
    if x % 2 == 0:
        print("Положительное четное число")
    else:
        print("Положительное нечетное число")
else:
    if x % 2 == 0:
        print("Отрицательное четное число")
    else:
        print("Отрицательное нечетное число")