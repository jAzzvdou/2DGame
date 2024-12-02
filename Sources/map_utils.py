import pygame
from utils import err
from macros import ERR_FILENAME, ERR_NOTFOUND, IMAGE, WALL, WAY, COIN, EXIT, PLAYER, ENEMY, DEATH


def get_map():
    '''
        Função para pegar o mapa do arquivo
    '''
    filename = str(input("Digite o nome do arquivo do mapa (ex: file.map): "))
    if (not filename.endswith('.map')):
        err(ERR_FILENAME.format(filename=filename))
        return None

    filename = '../Maps/' + filename
    try:
        with open(filename, 'r') as file:
            maps = [list(line.strip()) for line in file]
        return maps
    except FileNotFoundError:
        err(ERR_NOTFOUND.format(filename=filename))
        return None
    return None


def create_map(maps):
    '''
        Função para criar o mapa na tela.
    '''
    pygame.init()
    width = len(maps[0]) * IMAGE
    height = len(maps) * IMAGE

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("| O Castelo Arruinado |")

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


def update_map(screen, c, x, y):
    '''
        Função para atualizar o mapa na tela.
        Entra a tela, o caractere que você quer atualizar para tal, a posição x e y.
    '''
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
    elif (c == 'D'):
        screen.blit(DEATH, (x * IMAGE, y * IMAGE))
    pygame.display.update(pygame.Rect(x * IMAGE, y * IMAGE, IMAGE, IMAGE))
