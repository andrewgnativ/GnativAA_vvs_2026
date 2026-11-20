class Player:
    '''Игрок в лабиринте'''
    x = 0
    y = 0
    hp = 100
    inventory = None

def make_player(x, y):
    '''Создать игрока'''
    new_player = Player()
    new_player.x = x
    new_player.y = y
    new_player.hp = 100
    new_player.inventory = []
    return new_player

def player_pos(player):
    '''Координаты игрока кортежем'''
    return (player.x, player.y)

def try_move(player, dv, n, m):
    '''Попытка сдвинуть игрока'''
    new_x = player.x
    new_y = player.y
    if dv == 'w':
        new_x = new_x-1
    elif dv == 's':
        new_x = new_x+1
    elif dv == 'a':
        new_y = new_y-1
    elif dv == 'd':
        new_y = new_y+1
    else:
        return False

    if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
        return False

    player.x = new_x
    player.y = new_y
    return True
