from macros import ERR_IMAGE
from utils import err, count_char
import pygame
import random

try:
    WALL = pygame.image.load('../Textures/wall.png')
    WAY = pygame.image.load('../Textures/way.png')
    COIN = pygame.image.load('../Textures/coin.png')
    EXIT = pygame.image.load('../Textures/exit.png')
    PLAYER = pygame.image.load('../Textures/player.png')
    ENEMY = pygame.image.load('../Textures/enemy.png')
except pygame.error as error:
    err(ERR_IMAGE.format(image=error))

IMAGE = 64


def start_map(maps):
    pygame.init()
    width = len(maps[0]) * IMAGE
    height = len(maps) * IMAGE

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("| Ruined Castle |")

    for y, line in enumerate(maps):
        for x, i in enumerate(line):
            if (i == '1'):
                screen.blit(WALL, (x * IMAGE, y * IMAGE))
            elif (i == '0'):
                screen.blit(WAY, (x * IMAGE, y * IMAGE))
            elif (i == 'C'):
                screen.blit(COIN, (x * IMAGE, y * IMAGE))
            elif (i == 'E'):
                screen.blit(EXIT, (x * IMAGE, y * IMAGE))
            elif (i == 'P'):
                screen.blit(PLAYER, (x * IMAGE, y * IMAGE))
            elif (i == 'G'):
                screen.blit(ENEMY, (x * IMAGE, y * IMAGE))
    pygame.display.flip()
    return screen


def find_player(maps):
    for y, line in enumerate(maps):
        for x, i in enumerate(line):
            if (i == 'P'):
                return (x, y)
    return None


def update_map(screen, c, x, y):
    if (c == '0'):
        screen.blit(WAY, (x * IMAGE, y * IMAGE))
    elif (c == '1'):
        screen.blit(WALL, (x * IMAGE, y * IMAGE))
    elif (c == 'C'):
        screen.blit(COIN, (x * IMAGE, y * IMAGE))
    elif (c == 'E'):
        screen.blit(EXIT, (x * IMAGE, y * IMAGE))
    elif (c == 'P'):
        screen.blit(PLAYER, (x * IMAGE, y * IMAGE))
    elif (c == 'G'):
        screen.blit(ENEMY, (x * IMAGE, y * IMAGE))
    pygame.display.update(pygame.Rect(x * IMAGE, y * IMAGE, IMAGE, IMAGE))


def enemy_around(maps, x, y):
    if (maps[y - 1][x] == 'G' or maps[y + 1][x] == 'G'):
        return True
    elif (maps[y][x - 1] == 'G' or maps[y][x + 1] == 'G'):
        return True
    elif (maps[y - 1][x - 1] == 'G' or maps[y + 1][x + 1] == 'G'):
        return True
    elif (maps[y - 1][x + 1] == 'G' or maps[y + 1][x - 1] == 'G'):
        return True
    return False


def get_around(maps, x, y):
    around = []
    if (maps[y - 1][x] == 'G'):
        around.append((x, y - 1))
    if (maps[y + 1][x] == 'G'):
        around.append((x, y + 1))
    if (maps[y][x - 1] == 'G'):
        around.append((x - 1, y))
    if (maps[y][x + 1] == 'G'):
        around.append((x + 1, y))
    if (maps[y - 1][x - 1] == 'G'):
        around.append((x - 1, y - 1))
    if (maps[y + 1][x + 1] == 'G'):
        around.append((x + 1, y + 1))
    if (maps[y - 1][x + 1] == 'G'):
        around.append((x + 1, y - 1))
    if (maps[y + 1][x - 1] == 'G'):
        around.append((x - 1, y + 1))
    return around


def move_enemies(maps, screen):
    for y, line in enumerate(maps):
        for x, i in enumerate(line):
            if (i == 'G'):
                newx, newy = x, y
                direction = random.choice([0, 1, 2, 3])
                tempx, tempy = newx, newy
                if (direction == 0):
                    tempy -= 1
                elif (direction == 1):
                    tempy += 1
                elif (direction == 2):
                    tempx -= 1
                elif (direction == 3):
                    tempx += 1

                if (0 <= tempy < len(maps) and 0 <= tempx < len(maps[0])):
                    if (maps[tempy][tempx] == '0'):
                        newx, newy = tempx, tempy
                    elif (maps[tempy][tempx] == 'P'):
                        return None

                maps[y][x] = '0'
                update_map(screen, '0', x, y)
                maps[newy][newx] = 'G'
                update_map(screen, 'G', newx, newy)
    return maps


def map_loop(screen, maps):
    player = find_player(maps)
    coins = count_char(maps, 'C')

    running = True
    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
            elif (event.type == pygame.KEYDOWN):
                newx, newy = player
                if (event.key == pygame.K_ESCAPE):
                    return "exit"
                elif (event.key == pygame.K_UP):
                    newy -= 1
                elif (event.key == pygame.K_DOWN):
                    newy += 1
                elif (event.key == pygame.K_LEFT):
                    newx -= 1
                elif (event.key == pygame.K_RIGHT):
                    newx += 1
                elif (event.key == pygame.K_SPACE and enemy_around(maps, *player)):
                    enemies_around = get_around(maps, *player)
                    if (enemies_around):
                        for enemy in enemies_around:
                            update_map(screen, '0', *enemy)
                            maps[enemy[1]][enemy[0]] = '0'
                        continue

                if (maps[newy][newx] == 'E'):
                    if (coins < 1):
                        running = False
                        return "win"
                    else:
                        continue

                if (maps[newy][newx] == 'G'):
                    return "lose"

                if (maps[newy][newx] != '1'):
                    maps = move_enemies(maps, screen)
                    if (maps is None):
                        return "lose"
                    if (maps[newy][newx] == 'C'):
                        maps[newy][newx] = '0'
                        coins -= 1
                    if (maps[newy][newx] != 'E'):
                        update_map(screen, '0', *player)
                    player = (newx, newy)
                    update_map(screen, 'P', newx, newy)

        pygame.time.delay(100)

    pygame.quit()
    return "exit"
