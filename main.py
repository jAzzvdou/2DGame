from verify_map import get_map, invalid_map

def main():
    
    maps = get_map()
    if (maps is None):
        return
    if (invalid_map(maps)):
        return

    # start_map(maps)
    # map_loop()
