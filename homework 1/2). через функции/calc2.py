from functions4 import *

a = int(input('Введите первое число: '))
b = str(input('Введите знак операции: '))
c = int(input('Введите второе число: '))

print('Ответ:', end=' ')

if b == '+':
    print(summa(a, c))
elif b == '-':
    print(raznost(a, c))
elif b == '*':
    print(proizvedenie(a, c))
elif b == '/':
    print(delenie(a, c))
else:
    print('Введены неверные значения!')
