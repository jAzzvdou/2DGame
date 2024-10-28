from verify_map import get_map, invalid_map
from macros import ERR_IMAGE
from utils import err, count_char
import pygame

try:
    WALL = pygame.image.load('Textures/wall.png')
    WAY = pygame.image.load('Textures/way.png')
    COIN = pygame.image.load('Textures/coin.png')
    EXIT = pygame.image.load('Textures/exit.png')
    PLAYER = pygame.image.load('Textures/player.png')
except pygame.error as error:
    err(ERR_IMAGE.format(image=error))

IMAGE = 64


def start_map(maps):
    width = len(maps[0]) * IMAGE
    height = len(maps) * IMAGE

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game of Coins")

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
    elif (c == 'C'):
        screen.blit(COIN, (x * IMAGE, y * IMAGE))
    elif (c == 'E'):
        screen.blit(EXIT, (x * IMAGE, y * IMAGE))
    elif (c == 'P'):
        screen.blit(PLAYER, (x * IMAGE, y * IMAGE))
    pygame.display.update(pygame.Rect(x * IMAGE, y * IMAGE, IMAGE, IMAGE))


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
                if (event.key == pygame.K_UP):
                    newy -= 1
                elif (event.key == pygame.K_DOWN):
                    newy += 1
                elif (event.key == pygame.K_LEFT):
                    newx -= 1
                elif (event.key == pygame.K_RIGHT):
                    newx += 1

                if (maps[newy][newx] == 'E'):
                    if (coins < 1):
                        running = False
                        print("Congratulations! You won!")
                        break
                    else:
                        continue
                if (maps[newy][newx] != '1'):
                    if (maps[newy][newx] == 'C'):
                        maps[newy][newx] = '0'
                        coins -= 1
                    if (maps[newy][newx] != 'E'):
                        update_map(screen, '0', *player)
                    player = (newx, newy)
                    update_map(screen, 'P', newx, newy)

        pygame.time.delay(100)

    pygame.quit()


def main():
    maps = get_map()
    if (maps is None or invalid_map(maps)):
        return

    pygame.init()
    screen = start_map(maps)
    map_loop(screen, maps)


if __name__ == '__main__':
    main()
