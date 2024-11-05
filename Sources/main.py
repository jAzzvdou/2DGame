from verify_map import get_map, invalid_map
from start_map import start_map, map_loop


def main():
    maps = get_map()
    if (maps is None or invalid_map(maps)):
        return

    screen = start_map(maps)
    map_loop(screen, maps)


if __name__ == '__main__':
    main()
