import sys
from macros import YELLOW, RESET


def err(s):
    '''
        Função para printar mensagens de erro na saída de erro.
    '''
    message = YELLOW + s + RESET
    print(message, file=sys.stderr)


def count_char(maps, c):
    '''
        Função para contar a quantidade de um caractere no mapa.
    '''
    count = sum(line.count(c) for line in maps)
    return count
