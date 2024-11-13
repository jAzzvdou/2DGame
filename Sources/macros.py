import pygame
import sys

# ----------| ERRORS |---------- #
ERR_FILENAME = "Erro! '{filename}' é invalido. A extensão deve ser '.map'."
ERR_NOTFOUND = "Erro! Mapa '{filename}' não encontrado."
ERR_MAP = "Erro! Mapa inválido."
ERR_IMAGE = "Erro! Imagem '{image}' é inválida."

# ----------| COLORS |---------- #
CLEAR = "\033[H\033[J"
GREEN = "\033[92m"
RED = "\033[91m"
GREY = "\033[90m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# ----------| IMAGES |---------- #


def err(s):
    message = YELLOW + s + RESET
    print(message, file=sys.stderr)


try:
    WALL = pygame.image.load('../Textures/wall.png')
    WAY = pygame.image.load('../Textures/way.png')
    COIN = pygame.image.load('../Textures/coin.png')
    EXIT = pygame.image.load('../Textures/exit.png')
    PLAYER = pygame.image.load('../Textures/player.png')
    ENEMY = pygame.image.load('../Textures/enemy.png')
    DEATH = pygame.image.load('../Textures/death.png')
except pygame.error as error:
    err(ERR_IMAGE.format(image=error))

IMAGE = 64
