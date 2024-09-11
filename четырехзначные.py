
number = int(input("Введите четырехзначное число: "))
#проверка на четырехзначность
if number/1000>=1 and number<10000:
    print("YES")
else:
    print('NO')