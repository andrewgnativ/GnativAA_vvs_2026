def f(a, c, b):
    '''Вернуть результат действия с двумя числами'''
    if b == '+':
        return a + c
    elif b == '-':
        return a - c
    elif b == '*':
        return a * c
    else:
        return a / c
