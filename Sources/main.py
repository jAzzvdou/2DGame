from verify_map import get_map, invalid_map
from start_map import start_map, map_loop
from map_generator import generate_valid_map
from utils import err
from macros import OPTION, CLEAR
import random


def game(option):
    if (option == "1"):
        phase = 1
        while True:
            maps = generate_valid_map(
                random.randint(5, 15), random.randint(5, 15))
            if (maps is None or invalid_map(maps)):
                return

            screen = start_map(maps)
            result = map_loop(screen, maps)

            if (result == "win"):
                phase += 1
                print(f"\nParabéns! Você está na fase {phase}!")
                continue
            elif (result == "lose" or result == "exit"):
                if (result == "lose"):
                    print(f"\nVocê perdeu! Você chegou na fase {phase}!")
                elif (result == "exit"):
                    print(f"\nSaindo... Você chegou na fase {phase}!")
                break

    elif (option == "2"):
        maps = get_map()
        if (maps is None or invalid_map(maps)):
            return

        screen = start_map(maps)
        result = map_loop(screen, maps)

        if (result == "win"):
            print("\nParabéns! Você venceu!")
        elif (result == "lose"):
            print("\nVocê perdeu!")
        elif (result == "exit"):
            print("\nSaindo...")
    else:
        err("\nOpção inválida!")
        return


def main():
    print(CLEAR)
    user_input = str(input(OPTION))
    game(user_input)


if __name__ == '__main__':
    main()
