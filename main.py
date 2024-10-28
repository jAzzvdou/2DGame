from verify_map import get_map, invalid_map
from macros import ERR_IMAGE
from utils import err
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


def main():
    maps = get_map()
    if (maps is None):
        return
    if (invalid_map(maps)):
        return

    pygame.init()
    start_map(maps)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
