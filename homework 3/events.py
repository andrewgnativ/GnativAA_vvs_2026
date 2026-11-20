import random
from items import make_item, item_str, inventory_str

def get_weapon_damage(player):
    '''Суммарный бонус урона от оружия в инвентаре'''
    total = 0
    for item in player.inventory:
        if item.type == 'weapon':
            total += item.props.get('damage', 0)
    return total

def get_block(player):
    '''Суммарный блок от брони в инвентаре'''
    total = 0
    for item in player.inventory:
        if item.type == 'armor':
            total += item.props.get('block', 0)
    return total

def player_has_key(player):
    '''Есть ли ключ в инвентаре'''
    names = [item.name for item in player.inventory]
    return 'Ключ' in names

def change_room(room, player, labirint, visited):
    '''Обработать события в комнате при ПЕРВОМ входе'''
    print()
    if room.type == 'empty':
        print('Пустая комната, ничего интересного')
    elif room.type == 'start':
        print('Это стартовая комната')
    elif room.type == 'chest':
        change_chest(room, player)
    elif room.type == 'key':
        change_key_room(room, player)
    elif room.type == 'monster':
        change_monster(room, player)
    elif room.type == 'trap':
        change_trap(room, player)
    elif room.type == 'portal':
        change_portal(room, player, labirint, visited)
    elif room.type == 'exit':
        print('Выход! Нужен ключ')

def change_chest(room, player):
    '''Сундук: забрать 1 предмет или несколько'''
    if not room.items:
        print('Сундук пуст')
        return

    print('В сундуке лежит: ' + inventory_str(room.items))
    answer = input('Забрать всё? (да/нет): ').lower()
    if answer != 'да':
        print('Вы оставили предметы в сундуке')
        return
    if len(room.items) == 1:
        player.inventory.append(room.items[0])
        print('Добавлено: ' + item_str(room.items[0]))
    else:
        player.inventory.extend(room.items)
        print('Добавлено предметов: ' + str(len(room.items)))
    room.items = []

def change_key_room(room, player):
    '''Комната с ключом: забрать ключ'''
    if not room.items:
        print('Здесь уже пусто')
        return

    print('В комнате находится ключ')
    answer = input('Забрать ключ? (да/нет): ').lower()
    if answer != 'да':
        print('Ключ остался на месте')
        return
    player.inventory.append(room.items[0])
    room.items = []
    print('Ключ добавлен в инвентарь')

def change_monster(room, player):
    '''Бой с монстром'''
    if room.data.get('defeated'):
        print('Здесь лежит побеждённый монстр')
        return
    if 'hp' not in room.data:
        room.data['hp'] = random.randint(20, 40)
    monster_hp = room.data['hp']
    print('Монстр! У него ' + str(monster_hp) + ' HP')

    while monster_hp > 0 and player.hp > 0:
        print('Монстр: ' + str(monster_hp) + ' HP | Вы: ' + str(player.hp) + ' HP')
        command = input('1 - атака, 2 - предмет, 3 - бег: ')
        if command == '1':
            damage = random.randint(5, 12) + get_weapon_damage(player)
            monster_hp -= damage
            print('Вы нанесли ' + str(damage) + ' урона')
        elif command == '2':
            use_item_in_combat(player)
        elif command == '3':
            if random.random() < 0.5:
                print('Вы сбежали!')
                room.data['hp'] = monster_hp
                return
            print('Не удалось сбежать!')
        else:
            continue

        if monster_hp > 0:
            incoming_damage = random.randint(3, 12) - get_block(player)
            if incoming_damage < 0:
                incoming_damage = 0
            player.hp -= incoming_damage
            print('Монстр бьёт на ' + str(incoming_damage))

    if monster_hp <= 0:
        print('Монстр побеждён!')
        room.data['defeated'] = True
        reward_item = make_item('Золото', 'treasure', {'amount': 25})
        player.inventory.append(reward_item)
        print('Награда: ' + item_str(reward_item))

def use_item_in_combat(player):
    '''Использовать предмет из инвентаря'''
    if not player.inventory:
        print('Инвентарь пуст!')
        return
    print('Инвентарь: ')
    for i in range(len(player.inventory)):
        print(' ' + str(i) + ': ' + item_str(player.inventory[i]))
    answer = input('Индекс предмета (Enter - отмена): ')
    if answer == '':
        return
    try:
        item_index = int(answer)
    except ValueError:
        print('Нужно число!')
        return
    if item_index < 0 or item_index >= len(player.inventory):
        print('Неверный индекс!')
        return
    used_item = player.inventory[item_index]
    if used_item.type == 'potion':
        heal_amount = used_item.props.get('heal', 0)
        player.hp += heal_amount
        player.inventory.pop(item_index)
        print('Использовано: ' + used_item.name + ', +' + str(heal_amount) + ' HP')
    else:
        print('Этот предмет нельзя использовать в бою!')

def change_trap(room, player):
    '''Ловушка: урон, смягчается щитом'''
    if room.data.get('triggered'):
        print('Ловушка уже сработала')
        return
    damage = random.randint(10, 25)
    block_value = get_block(player)
    final_damage = damage - block_value
    if final_damage < 0:
        final_damage = 0
    print('Ловушка! Урон: ' + str(damage) + ', блок: ' + str(block_value))
    player.hp -= final_damage
    room.data['triggered'] = True
    print('Потеряно ' + str(final_damage) + ' HP')

def change_portal(room, player, labirint, visited):
    '''Портал: телепорт в другой портал'''
    rows_count = len(labirint)
    cols_count = len(labirint[0])
    other_portals = []
    for row in range(rows_count):
        for col in range(cols_count):
            if labirint[row][col].type == 'portal' and (row, col) != (player.x, player.y):
                other_portals.append((row, col))
    if not other_portals:
        print('Портал никуда не ведёт - других порталов нет')
        return

    destination = random.choice(other_portals)
    print('Портал! Вас телепортирует в (' + str(destination[0]) + ', ' + str(destination[1]) + ')')
    player.x = destination[0]
    player.y = destination[1]
    visited[destination[0]][destination[1]] = True

def use_mana_potion_on_weapon(player, potion_idx, weapon_idx):
    '''Применить зелье маны к оружию: +урон; меняется свойство предмета'''
    potion = player.inventory[potion_idx]
    weapon = player.inventory[weapon_idx]

    if potion.type != 'mana_potion':
        print('Это не зелье маны!')
        return

    if weapon.type != 'weapon':
        print('Маной можно усилить только оружие!')
        return

    bonus_damage = potion.props.get('mana', 10)
    old_damage = weapon.props.get('damage', 0)
    weapon.props['damage'] = old_damage + bonus_damage
    player.inventory.pop(potion_idx)
    print('Меч усилен! damage: ' + str(old_damage) + ' -> ' + str(old_damage + bonus_damage))

def use_heal_potion_outside_combat(player, idx):
    '''Выпить зелье здоровья вне боя'''
    if idx < 0 or idx >= len(player.inventory):
        print('Неверный индекс!')
        return
    item = player.inventory[idx]
    if item.type != 'potion':
        print('Это не зелье здоровья!')
        return
    heal_amount = item.props.get('heal', 0)
    player.hp = player.hp + heal_amount
    player.inventory.pop(idx)
    print('Выпито: +' + str(heal_amount) + ' HP, теперь HP = ' + str(player.hp))
