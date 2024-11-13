import pygame
from utils import count_char
from map_utils import get_map, create_map, update_map
from verify_map import invalid_map
from macros import GREEN, RED, GREY, RESET


def init_game():
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
    for y, line in enumerate(maps):
        for x, i in enumerate(line):
            if (i == 'P'):
                return (x, y)
    return None


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


def gameplay(screen, maps):
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
                            update_map(screen, 'D', *enemy)
                            pygame.time.delay(100)
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
