import sys
from macros import *
from utils import *

def get_map():
    filename = str(input("Digite o nome do arquivo do mapa (ex: map.ber): "))
    if (not filename.endswith('.map'))
        err(ERR_FILENAME.format(filename=filename))
        return None

    try:
        with open(filename, 'r') as file:
            maps = [list(line.strip()) for line in file] # OLHAR.
        return maps
    except FileNotFoundError:
        err(ERR_NOTFOUND.format(filename=filename))
        return None

    return None


def isnt_rectangular(maps):
    linelen = len(maps[0])
    for line in maps:
        if (len(line) != linelen):
            return True
    return False


def invincible_map(maps):
    player_pos = None
    exit_pos = None
    coin_pos = set()

    for y, line in enumerate(maps):
        for x, i in enumerate(line):
            if (i == 'P'):
                player_pos = (y, x)
            elif (i == 'E'):
                exit_pos = (y, x)
            elif (i == 'C'):
                coin_pos.add((y, x))

    def floodfill(visited, y, x):
        if ((y, x) in visited or maps[y][x] == '1'):
            return

        visited.add((y, x))
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for directy, directx in directions:
            newy, newx = y + directy, x + directx
            if ((0 <= newy < len(maps)) and (0 <= newx < len(maps[0]))):
                floodfill(newy, newx, visited)

    visited = set()
    floodfill(player_pos[0], player_pos[1], visited)
    if (not coin_pos.issubset(visited) or (exit_pos not in visited)):
        return True
    
    return False


def invalid_map(maps):
    player = count_char(maps, 'P') != 1
    exitt = count_char(maps, 'E') != 1
    coin = count_char(maps, 'C') < 1

    if (player or exitt or coin or isnt_rectangular(maps)):
        err(ERR_MAP)
        return True

    if ((not all(i == '1' for i in maps[0]) or (not all(i == '1' for i in maps[-1])):
         err(ERR_MAP)
         return True

    for line in maps:
        if (line[0] != '1' or line[-1] != '1'):
            err(ERR_MAP)
            return True

    if (invincible_map(maps)):
        err(ERR_MAP)
        return True

