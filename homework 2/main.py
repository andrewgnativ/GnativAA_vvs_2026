from functions import *

while True:
    print('Введите номер уровня: ', end='')
    try:
        level_number = int(input())
    except ValueError:
        print('Данные некорректны!')
        continue
    if level_number == 1:
        def1()
    elif level_number == 2:
        def2()
    elif level_number == 3:
        def3()
    elif level_number == 4:
        def4()
    elif level_number == 5:
        def5()
    else:
        print('Такого уровня не существует!')
    answer_continue = str(input('Продолжить? Введите "да" или "нет": '))
    if answer_continue.strip().lower() == 'нет':
        break
