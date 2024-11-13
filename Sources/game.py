import pygame
from utils import count_char
from map_utils import get_map, create_map, update_map
from verify_map import invalid_map
from macros import GREEN, RED, GREY, RESET


def init_game():
    '''
        Função que inicializa o mapa e o jogo.
    '''
    maps = get_map()
    if (maps is None or invalid_map(maps)):
        return
    screen = create_map(maps)
    result = gameplay(screen, maps)
    if (result == "win"):
        print(GREEN + "\nParabéns! Você venceu!" + RESET)
    elif (result == "lose"):
        print(RED + "\nVocê perdeu!" + RESET)
    elif (result == "exit"):
        print(GREY + "\nSaindo..." + RESET)


def find_player(maps):
    '''
        Função para encontrar a posição do jogador no mapa.
    '''
    for y, line in enumerate(maps):
        for x, i in enumerate(line):
            if (i == 'P'):
                return (x, y)
    return None


def enemy_around(maps, x, y):
    '''
        Função para verificar se tem inimigos ao redor do jogador.
    '''
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
    '''
        Função para pegar as posições dos inimigos ao redor do jogador.
    '''
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


def gameplay(screen, maps):
    '''
        Função para o gameplay do jogo, movimentação e ataque do jogador.
    '''
    player = find_player(maps)
    coins = count_char(maps, 'C')

    print("O jogo iniciou!")
    running = True
    while running:
        print("Dentro do While True...")
        for event in pygame.event.get():
            print("Dentro do For Event...")
            if (event.type == pygame.QUIT):
                running = False
            elif (event.type == pygame.KEYDOWN):
                print("1")
                newx, newy = player
                if (event.key == pygame.K_ESCAPE):
                    print("2")
                    return "exit"
                elif (event.key == pygame.K_UP):
                    print("3")
                    newy -= 1
                elif (event.key == pygame.K_DOWN):
                    print("4")
                    newy += 1
                elif (event.key == pygame.K_LEFT):
                    print("5")
                    newx -= 1
                elif (event.key == pygame.K_RIGHT):
                    print("6")
                    newx += 1
                elif (event.key == pygame.K_SPACE and enemy_around(maps, *player)):
                    print("7")
                    enemies_around = get_around(maps, *player)
                    if (enemies_around):
                        print("8")
                        for enemy in enemies_around:
                            print("9")
                            update_map(screen, 'D', *enemy)
                            pygame.time.delay(100)
                            update_map(screen, '0', *enemy)
                            maps[enemy[1]][enemy[0]] = '0'
                        continue

                print("10")
                if (maps[newy][newx] == 'E'):
                    if (coins < 1):
                        print("11")
                        running = False
                        return "win"
                    else:
                        print("12")
                        continue

                print("13")
                if (maps[newy][newx] == 'G'):
                    return "lose"

                print("14")
                if (maps[newy][newx] != '1'):
                    if (maps[newy][newx] == 'C'):
                        maps[newy][newx] = '0'
                        coins -= 1
                    if (maps[newy][newx] != 'E'):
                        update_map(screen, '0', *player)
                    player = (newx, newy)
                    update_map(screen, 'P', newx, newy)
                print("Atualizando tela...")

        pygame.time.delay(100)

    pygame.quit()
    return "exit"
