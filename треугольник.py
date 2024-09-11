a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if a+b>c and a+c>b and b+c>a:
    print('YES')
else:
    print('NO')