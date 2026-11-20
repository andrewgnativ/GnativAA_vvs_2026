import random
from labirint import generate_labirint, show_labirint
from player import make_player, player_pos, try_move
from items import inventory_str
from events import change_room, player_has_key
from inventory import open_inventory

def main():
    # random.seed(1)
    n, m = 10, 10
    labirint, visited = generate_labirint(n, m)
    player = make_player(0, 0)
    visited[0][0] = True

    while True:
        print()
        show_labirint(labirint, visited, player_pos(player), n, m)
        print('HP:', player.hp, '| Ключ:', 'да' if player_has_key(player) else 'нет')
        print('Инвентарь:', inventory_str(player.inventory))
        print('w/a/s/d - идти, i - инвентарь, q - выход')

        command = input('Ваш ход: ').lower()
        if command == 'q':
            print('Пока!')
            break
        if command == 'i':
            open_inventory(player)
            continue
        if not try_move(player, command, n, m):
            print('Туда нельзя!')
            continue

        player_row, player_col = player_pos(player)

        if player_row == n - 1 and player_col == m - 1 and player_has_key(player):
            print()
            print('==========================================')
            print('     ПОБЕДА! Вы открыли выход ключом!')
            print('==========================================')
            break

        if not visited[player_row][player_col]:
            visited[player_row][player_col] = True
            change_room(labirint[player_row][player_col], player, labirint, visited)
            if player.hp <= 0:
                print('\nВы умерли. HP: ' + str(player.hp))
                break

main()
