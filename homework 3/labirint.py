import random
import copy
from items import make_item

class Room:
    '''Одна клетка лабиринта'''
    type = ''
    items = None
    data = None

def make_room(type_, items, data):
    '''Создать комнату'''
    room = Room()
    room.type = type_
    room.items = items
    room.data = data
    return room

#Легенда карты
icons = {
    'start': 'S',
    'exit': 'E',
    'empty': '.',
    'chest': 'C',
    'monster': 'M',
    'trap': 'T',
    'key': 'K',
    'portal': 'P',
}
player_icon = '@'
unknown_icon = '?'
room_types = ['empty', 'chest', 'monster', 'trap', 'portal']
loot = [
    ('Золото', 'treasure', {'amount': 50}),
    ('Зелье здоровья', 'potion', {'heal': 30}),
    ('Зелье маны', 'mana_potion', {'mana': 10}),
    ('Меч', 'weapon', {'damage': 10}),
    ('Щит', 'armor', {'block': 5}),
    ('Свиток', 'scroll', {}),
    ]



def generate_labirint(n, m):
    '''Сгенерировать лабиринт n*m'''
    labirint = []
    for row_index in range(n):
        row_rooms = []
        for col_index in range(m):
            room = make_room(random.choice(room_types), [], {})
            row_rooms.append(room)
        labirint.append(row_rooms)

    visited_map = []
    for row_index in range(n):
        row_rooms = []
        for col_index in range(m):
            row_rooms.append(False)
        visited_map.append(row_rooms)

    labirint[0][0].type = 'start'
    labirint[n-1][m-1].type = 'exit'

    free_cells = []
    for row_index in range(n):
        for col_index in range(m):
            if not(row_index == 0 and col_index == 0) and not(row_index == n-1 and col_index == m-1):
                free_cells.append((row_index, col_index))
    key_row, key_col = random.choice(free_cells)
    labirint[key_row][key_col].type = 'key'
    labirint[key_row][key_col].items = [make_item('Ключ', 'key', {})]

    for row_index in range(n):
        for col_index in range(m):
            if labirint[row_index][col_index].type == 'chest':
                if random.random() < 0.3:
                    labirint[row_index][col_index].items = []
                else:
                    items_count = random.randint(1, 3)
                    chosen_loot = random.sample(loot, items_count)
                    chest_items = []
                    for item_name, item_type, item_props in chosen_loot:
                        chest_items.append(make_item(item_name, item_type, copy.deepcopy(item_props)))
                    labirint[row_index][col_index].items = chest_items
    
    return labirint, visited_map

def show_labirint(labirint, visited, pos, n, m):
    '''Нарисовать лабиринт'''
    for row_index in range(n):
        row_string = ''
        for col_index in range(m):
            if (row_index, col_index) == pos:
                row_string += player_icon + ' '
            elif visited[row_index][col_index]:
                row_string += icons[labirint[row_index][col_index].type] + ' '
            else:
                row_string += unknown_icon + ' '
        print(row_string)
