from verify_map import invalid_map
import random


def generate_map(width, height):
    maps = [['1'] * width for _ in range(height)]
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            maps[y][x] = '0' if random.random() > 0.3 else '1'

    player_x, player_y = random.randint(1, width - 2), random.randint(1, height - 2)
    maps[player_y][player_x] = 'P'

    exit_x, exit_y = random.randint(1, width - 2), random.randint(1, height - 2)
    while (exit_x, exit_y) == (player_x, player_y):
        exit_x, exit_y = random.randint(1, width - 2), random.randint(1, height - 2)
    maps[exit_y][exit_x] = 'E'

    num_coins = random.randint(1, 5)
    num_enemies = random.randint(1, 5)

    for _ in range(num_coins):
        coin_x, coin_y = random.randint(1, width - 2), random.randint(1, height - 2)
        while maps[coin_y][coin_x] != '0':
            coin_x, coin_y = random.randint(1, width - 2), random.randint(1, height - 2)
        maps[coin_y][coin_x] = 'C'

    for _ in range(num_enemies):
        enemy_x, enemy_y = random.randint(1, width - 2), random.randint(1, height - 2)
        while maps[enemy_y][enemy_x] != '0':
            enemy_x, enemy_y = random.randint(1, width - 2), random.randint(1, height - 2)
        maps[enemy_y][enemy_x] = 'G'

    return maps


def generate_valid_map(width, height):
    while True:
        maps = generate_map(width, height)
        if not invalid_map(maps):
            return maps
        print("Mapa inválido, tentando novamente...")
