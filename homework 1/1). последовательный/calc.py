a = int(input('Введите первое число: '))
b = str(input('Введите знак операции: '))
c = int(input('Введите второе число: '))

print('Ответ:', end=' ')
if b == '+':
    print(a + c)
elif b == '-':
    print(a - c)
elif b == '*':
    print(a * c)
elif b == '/':
    print(a / c)
else:
    print('Введены неверные значения!')
