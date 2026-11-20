from functions1 import f

while True:
    try:
        a = int(input('Введите первое число: '))
    except ValueError:
        print('Нужно было ввести число!')
        break
    b = str(input('Введите знак операции: '))
    try:
        c = int(input('Введите второе число: '))
    except ValueError:
        print('Нужно было ввести число!')
        break
    if b == '/' and c == 0:
        print('На ноль делить нельзя!')
    elif b in ('+', '-', '*', '/'):
        print('Ответ:', f(a, c, b))
    else:
        print('Введены неверные значения!')
    answer_continue = str(input('Продолжить? '))
    if answer_continue.strip().lower() == 'нет':
        break
