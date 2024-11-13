from utils import err, count_char
from macros import ERR_MAP


def verify_chars(maps):
    '''
        Função para verificar se os caracteres do mapa são válidos.
    '''
    for line in maps:
        for i in line:
            if (i not in ['0', '1', 'C', 'E', 'P', 'G']):
                err(ERR_MAP)
                err("Caractere inválido.")
                return True
    return False


def isnt_rectangular(maps):
    '''
        Função para verificar se o mapa é retangular.
    '''
    linelen = len(maps[0])
    for line in maps:
        if (len(line) != linelen):
            return True
    return False


def quantity_chars(maps):
    '''
        Função para verificar se a quantidade de caracteres do mapa é válida.
    '''
    player = count_char(maps, 'P') != 1
    exitt = count_char(maps, 'E') != 1
    coin = count_char(maps, 'C') < 1
    if (player or exitt or coin or isnt_rectangular(maps)):
        err(ERR_MAP)
        err("O mapa não é retangular || player != 1, exit != 1, coin < 1.")
        return True


def verify_corners(maps):
    '''
        Função para verificar se as bordas do mapa são paredes.
    '''
    if ((not all(i == '1' for i in maps[0])) or (not all(i == '1' for i in maps[-1]))):
        err(ERR_MAP)
        err("As bordas do mapa devem ser paredes.")
        return True

    for line in maps:
        if (line[0] != '1' or line[-1] != '1'):
            err(ERR_MAP)
            err("As bordas do mapa devem ser paredes.")
            return True
    return False


def invincible_map(maps):
    '''
        Função para verificar se o mapa é invencível.
    '''
    player_pos = None
    coin_pos = set()
    exit_pos = None
    for y, line in enumerate(maps):
        for x, i in enumerate(line):
            if (i == 'P'):
                player_pos = (y, x)
            elif (i == 'C'):
                coin_pos.add((y, x))
            elif (i == 'E'):
                exit_pos = (y, x)

    def floodfill(y, x, visited, ignore_exit=True):
        if ((y, x) in visited or maps[y][x] == '1' or (ignore_exit and maps[y][x] == 'E')):
            return
        visited.add((y, x))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (0 <= ny < len(maps) and 0 <= nx < len(maps[0])):
                floodfill(ny, nx, visited, ignore_exit)

    visited = set()
    floodfill(player_pos[0], player_pos[1], visited, ignore_exit=True)
    if (not coin_pos.issubset(visited)):
        return True
    visited.clear()
    floodfill(player_pos[0], player_pos[1], visited, ignore_exit=False)
    if (exit_pos not in visited):
        return True
    return False


def invalid_map(maps):
    '''
        Função para verificar se o mapa é inválido.
    '''
    if (verify_chars(maps)):
        return True

    if (quantity_chars(maps)):
        return True

    if (verify_corners(maps)):
        return True

    if (invincible_map(maps)):
        err(ERR_MAP)
        err("O mapa é invencível.")
        return True
    return False
