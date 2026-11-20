import copy
from items import item_str, inventory_str
from events import use_mana_potion_on_weapon, use_heal_potion_outside_combat

type_order = {
    'weapon': 0,
    'armor': 1,
    'potion': 2,
    'mana_potion': 3,
    'key': 4,
    'scroll': 5,
    'treasure': 6,
}

def sort_key(item):
    '''Критерий сортировки: сначала по типу, потом по имени'''
    order = type_order.get(item.type, 99)
    return (order, item.name)

def find_index_by_name(player, name):
    '''Позиция предмета по имени через index(); -1, если нет'''
    item_names = [item.name for item in player.inventory]
    if name in item_names:
        return item_names.index(name)
    return -1

def open_inventory(player):
    '''Меню инвентаря, возвращает None'''
    while True:
        print()
        print('=== ИНВЕНТАРЬ ===')
        if not player.inventory:
            print('Пусто')
            print('0 - назад')
            command = input('> ')
            if command == '0':
                return
            continue

        for i in range(len(player.inventory)):
            print('  ' + str(i) + ': ' + item_str(player.inventory[i]))
        
        print('Действия:')
        print('  1 - выбросить по имени')
        print('  2 - выбросить по индексу')
        print('  3 - сортировать по типу и имени')
        print('  4 - сортировать по убыванию')
        print('  5 - перевернуть порядок')
        print('  6 - найти предмет')
        print('  7 - копия и срез')
        print('  8 - ДЕМОНСТРАЦИЯ: copy() VS deepcopy()')
        print('  9 - применить предмет к предмету')
        print('  0 - назад')

        command = input('> ')
        if command == '0':
            return

        elif command == '1':
            # remove по имени
            item_name = input('Имя предмета: ')
            item_names = [item.name for item in player.inventory]
            if item_name in item_names:
                for item in player.inventory:
                    if item.name == item_name:
                        player.inventory.remove(item)
                        print('Удалено: ' + item_str(item))
                        break
            else:
                print('Нет такого предмета')

        elif command == '2':
            # pop по индексу
            answer = input('Индекс: ')
            try:
                item_index = int(answer)
            except ValueError:
                print('Нужно число!')
                continue
            if item_index < 0 or item_index >= len(player.inventory):
                print('Неверный индекс!')
                continue
            removed_item = player.inventory.pop(item_index)
            print('Удалено: ' + item_str(removed_item))

        elif command == '3':
            # sort с критерием
            player.inventory.sort(key=sort_key)
            print('Отсортировано по типу и имени')

        elif command == '4':
            # sort(reverse=True): и sort, и reverse за раз
            player.inventory.sort(key=sort_key, reverse=True)
            print('Отсортировано по убыванию')

        elif command == '5':
            # reverse: переворачивает текущий порядок
            player.inventory.reverse()
            print('Порядок перевёрнут')

        elif command == '6':
            # index + in
            item_name = input('Что ищем? ')
            item_index = find_index_by_name(player, item_name)
            if item_index == -1:
                print('Не найдено')
            else:
                print('Найдено на позиции ' + str(item_index) + ': ' + item_str(player.inventory[item_index]))

        elif command == '7':
            # copy + slice
            inventory_copy = player.inventory.copy()
            print()
            print('Копия: ' + str(len(inventory_copy)) + ' предметов')
            print('  ' + inventory_str(inventory_copy))

            first_three_items = inventory_copy[:3]
            print('Первые три:')
            print('  ' + inventory_str(first_three_items))

            print()
            print('ВНИМАНИЕ: copy() — поверхностное!')
            print('Предметы в копии — те же объекты, что в оригинале.')
            print('Команда 8 покажет, почему это проблема.')

        elif command == '8':
            demonstrate_copy_problem(player)

        elif command == '9':
            # применить предмет к предмету
            print('Что применяем?')
            for i in range(len(player.inventory)):
                print('  ' + str(i) + ': ' + item_str(player.inventory[i]))
            answer1 = input('Индекс: ')
            try:
                first_index = int(answer1)
            except ValueError:
                print('Нужно число!')
                continue
            if first_index < 0 or first_index >= len(player.inventory):
                print('Неверный индекс!')
                continue
            
            selected_item = player.inventory[first_index]

            # зелье здоровья - применяется к игроку (второй индекс не нужен)
            if selected_item.type == 'potion':
                use_heal_potion_outside_combat(player, first_index)
                continue

            # зелье маны - применяется к оружию (нужен второй индекс)
            if selected_item.type == 'mana_potion':
                answer2 = input('К какому оружию? индекс: ')
                try:
                    second_index = int(answer2)
                except ValueError:
                    print('Нужно число!')
                    continue
                if second_index < 0 or second_index >= len(player.inventory):
                    print('Неверный индекс!')
                    continue
                use_mana_potion_on_weapon(player, first_index, second_index)
                continue
            
            print('Этот предмет нельзя применить')
        
        else:
            print('Нет такой команды')

def demonstrate_copy_problem(player):
    '''Показать разницу между copy() и deepcopy() на практике'''
    if not player.inventory:
        print('Инвентарь пуст — нечего копировать')
        return

    # ищем первый предмет, у которого есть хоть одно свойство (props)
    item_index = -1
    for i in range(len(player.inventory)):
        if player.inventory[i].props:
            item_index = i
            break

    if item_index == -1:
        print('Нет предметов со свойствами — не на чем демонстрировать')
        return

    property_key = None
    for key in player.inventory[item_index].props:
        property_key = key
        break
    old_property_value = player.inventory[item_index].props[property_key]

    print()
    print('=== ДЕМОНСТРАЦИЯ: copy() VS deepcopy() ===')
    print('Работаем с предметом: ' + item_str(player.inventory[item_index]))
    print('Свойство: ' + property_key + ' (сейчас ' + str(old_property_value) + ')')

    print()
    print('--- copy() (поверхностное) ---')
    shallow_copy = player.inventory.copy()
    print('Создана копия: .copy()')
    shallow_copy[item_index].props[property_key] = old_property_value + 100
    print('У копии поменяли ' + property_key + ': ' + str(old_property_value) + ' -> ' + str(old_property_value + 100))
    print()
    print('Что стало:')
    print('  Копия:    ' + inventory_str(shallow_copy))
    print('  Оригинал: ' + inventory_str(player.inventory))

    if player.inventory[item_index].props[property_key] == old_property_value + 100:
        print()
        print('!!! ПРОБЛЕМА: оригинал ТОЖЕ изменился!')
        print('copy() копирует только список, а предметы внутри - те же объекты')
        print('Поменяли в копии - поменяли и в оригинале')
        # восстанавливаем оригинал, чтобы игра не сломалась
        player.inventory[item_index].props[property_key] = old_property_value
        print('(восстановили оригинал на ' + str(old_property_value) + ')')

    print()
    print('--- deepcopy() (глубокое) ---')
    deep_copy = copy.deepcopy(player.inventory)
    print('Создана копия: copy.deepcopy()')
    deep_copy[item_index].props[property_key] = old_property_value + 100
    print('У копии поменяли ' + property_key + ': ' + str(old_property_value) + ' -> ' + str(old_property_value + 100))
    print()
    print('Что стало:')
    print('  Копия:    ' + inventory_str(deep_copy))
    print('  Оригинал: ' + inventory_str(player.inventory))

    if player.inventory[item_index].props[property_key] == old_property_value:
        print()
        print('Хмм, оригинал НЕ изменился - deepcopy скопировал и предметы тоже.')

    print()
    print('Вывод: в игре используем deepcopy, чтобы предметы в копиях были независимы')
    print('Именно так мы делаем в labirint.py при создании предметов из loot_pool')
