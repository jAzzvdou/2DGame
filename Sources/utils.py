import sys
from macros import YELLOW, RESET


def err(s):
    message = YELLOW + s + RESET
    print(message, file=sys.stderr)


def count_char(maps, c):
    count = sum(line.count(c) for line in maps)
    return count
