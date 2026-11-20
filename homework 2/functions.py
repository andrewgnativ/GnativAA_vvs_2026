def def1():
    example1 = str("пРиВет_МИР")
    print('', 'Добро пожаловать на уровень 1! Данный уровень рассматривает 3 метода изменения регистра в строке:',
          '1) строка.upper() - переводит все буквенные символы строки в верхний регистр;',
          '2) строка.lower() - переводит все буквенные символы строки в нижний регистр;',
          '3) строка.capitalize() - переводит первый символ строки в верхний регистр, остальные - в нижний.',
          '', 'Пример на строке "'+example1+'":', sep="\n")
    print('Метод upper():', example1.upper())
    print('Метод lower():', example1.lower())
    print('Метод capitalize():', example1.capitalize())
    print('', 'Введите номер метода, который хотите реализовать:', sep="\n")
    try:
        method_number = int(input())
        if method_number < 1 or method_number > 3:
            print('Данные некорректны!')
        else:
            source_string = str(input('Введите строку: '))
            if method_number == 1:
                print('Результат:', source_string.upper())
            elif method_number == 2:
                print('Результат:', source_string.lower())
            else:
                print('Результат:', source_string.capitalize())
    except ValueError:
        print('Данные некорректны!')


def def2():
    example2 = str("Ботать это круто. Очень круто")
    print('', 'Добро пожаловать на уровень 2! Данный уровень рассматривает 3 метода работы с подстроками:',
          '1) строка.find(подстрока) - возвращает индекс первого вхождения подстроки, а именно ее первого символа (или -1, если не найдено);',
          '2) строка.replace(старое, новое, кол-во) - возвращает новую строку c заменой всех (если не написать кол-во) или части вхождений подстроки;',
          '3) строка.count(подстрока) - считает, сколько раз подстрока встречается в строке (без перекрытий).',
          '', 'Пример на строке "'+example2+'":', sep="\n")
    print('Найдем позицию первого вхождения "круто" (метод find()):', example2.find('круто'))
    print('Заменим "круто" на символ "!" (метод replace()):', example2.replace('круто', '!'))
    print('Посчитаем все буквы "о" (метод count()):', example2.count('о'))
    print('', 'Введите номер метода, который хотите реализовать:', sep="\n")
    try:
        method_number = int(input())
        if method_number < 1 or method_number > 3:
            print('Данные некорректны!')
        else:
            if method_number == 1:
                source_string = str(input('Введите исходную строку: '))
                search_string = str(input('Введите искомую подстроку: '))
                print('Результат:', source_string.find(search_string))
            elif method_number == 2:
                source_string = str(input('Введите исходную строку: '))
                search_string = str(input('Введите подстроку, которую нужно заменить: '))
                replace_string = str(input('Введите подстроку, НА которую нужно заменить: '))
                replace_count = int(input('Введите кол-во замен (если нужно все, напишите "-1"): '))
                if replace_count < -1:
                    print('Данные некорректны!')
                elif replace_count == -1:
                    print('Результат:', source_string.replace(search_string, replace_string))
                else:
                    print('Результат:', source_string.replace(search_string, replace_string, replace_count))
            else:
                source_string = str(input('Введите исходную строку: '))
                search_string = str(input('Введите искомую подстроку: '))
                print('Результат:', source_string.count(search_string))
    except ValueError:
        print('Данные некорректны!')


def def3():
    example3_string = str("1,2,3,4")
    example3_list = ['1', '2', '3', '4']
    print('', 'Добро пожаловать на уровень 3! Данный уровень рассматривает методы разбиения и сборки строк:',
          '1) строка.split(разделитель) - разбивает строку на список подстрок по разделителю (по умолчанию - по пробелам);',
          '2) разделитель.join(список) - собирает строку из списка, вставляя между элементами разделитель.',
          '', 'Пример на строке "'+example3_string+'":', sep="\n")
    print('Разделим на список по разделителю "," (метод split()):', example3_string.split(','))
    print('', 'Пример на списке '+str(example3_list)+':', sep="\n")
    print('Соберем строку, вставляя разделитель "," (метод join()):', ','.join(example3_list))
    print('', 'Введите номер метода, который хотите реализовать:', sep="\n")
    try:
        method_number = int(input())
        if method_number < 1 or method_number > 2:
            print('Данные некорректны!')
        else:
            if method_number == 1:
                source_string = str(input('Введите исходную строку: '))
                separator = str(input('Введите разделитель (пробел тоже нужно ввести!): '))
                print('Результат:', source_string.split(separator))
            else:
                elements_count = int(input('Введите количество элементов исходного списка: '))
                if elements_count < 1:
                    print('Данные некорректны!')
                else:
                    print('Теперь по одному вводите каждый элемент:')
                    elements_list = []
                    for _ in range(elements_count):
                        elements_list.append(input())
                    separator = str(input('Введите разделитель (может отсутствовать): '))
                    print('Результат:', separator.join(elements_list))
    except ValueError:
        print('Данные некорректны!')


def def4():
    example4_chars = str("1234*&%^$")
    example4_spaces = str("    abc1234    ")
    print('', 'Добро пожаловать на уровень 4! Данный уровень рассматривает методы проверки и очистки строки:',
          '1) строка.isdigit() - проверяет, состоит ли строка только из цифр (True/False);',
          '2) строка.isalpha() - проверяет, состоит ли строка только из букв (True/False);',
          '3) строка.strip(символ) - убирает пробелы (или указанные символы) с начала и конца строки.',
          '', 'Пример на строке "'+example4_chars+'":', sep="\n")
    print('Метод isdigit():', example4_chars.isdigit())
    print('Метод isalpha():', example4_chars.isalpha())
    print('', 'Пример на строке "'+example4_spaces+'":', sep="\n")
    print('Метод strip(), по умолчанию - пробелы:', example4_spaces.strip())
    print('', 'Введите номер метода, который хотите реализовать:', sep="\n")
    try:
        method_number = int(input())
        if method_number < 1 or method_number > 3:
            print('Данные некорректны!')
        else:
            if method_number == 1:
                source_string = str(input('Введите строку: '))
                print('Результат:', source_string.isdigit())
            elif method_number == 2:
                source_string = str(input('Введите строку: '))
                print('Результат:', source_string.isalpha())
            else:
                source_string = str(input('Введите исходную строку: '))
                strip_chars = str(input('Введите убираемые символы строкой (пробел тоже нужно ввести!): '))
                print('Результат:', source_string.strip(strip_chars))
    except ValueError:
        print('Данные некорректны!')


def fix(test):
    text = test.strip()
    text = text.capitalize()
    text = text.replace('. ', '.').replace('.', '. ')
    text = text.replace(', ', ',').replace(',', ', ')
    text = text.replace(': ', ':').replace(':', ': ')
    text = text.replace('; ', ';').replace(';', '; ')
    text = text.replace('! ', '!').replace('!', '! ')
    text = text.replace('? ', '?').replace('?', '? ')
    text = text.strip()
    while '  ' in text:
        text = text.replace('  ', ' ')
    result_chars = []
    for index in range(len(text)):
        if index >= 2 and text[index-2] in '.!?' and text[index-1] == ' ':
            result_chars.append(text[index].upper())
        elif index < len(text)-1 and text[index] == ' ' and text[index+1] in '.!?;:,':
            pass
        else:
            result_chars.append(text[index])
    fixed_text = ''.join(result_chars)
    return fixed_text


def def5():
    example5 = str("        pYtHon;is.AWESome     ")
    print('', 'Добро пожаловать на уровень 5!',
          'Данный уровень превращает заданную строку в нормальный вид, используя методы из предыдущих уровней.',
          '', 'Пример на строке "'+example5+'":', sep="\n")
    print(fix(example5))
    print('', 'Введите строку, которую хотите исправить:', sep="\n")
    text = str(input())
    print('Результат:', fix(text))
