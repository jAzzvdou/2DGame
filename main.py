from verify_map import get_map, invalid_map
'''
import pygame

try:
    WALL = pygame.image.load('wall.png')
    WAY = pygame.image.load('way.png')
    COIN = pygame.image.load('coin.png')
    EXIT = pygame.image.load('exit.png')
    PLAYER = pygame.image.load('player.png')
except pygame.error as error:
    err(ERR_IMAGE.format(image=error))

IMAGE = 16

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

    pygames.display.flip()


# def map_loop(maps):
'''


def main():
    # pygame.init()

    maps = get_map()
    if (maps is None):
        return
    if (invalid_map(maps)):
        return

    print("O mapa é válido!")

    # start_map(maps)
    # map_loop(maps)


if __name__ == '__main__':
    main()
