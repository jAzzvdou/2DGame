import sys


def err(s):
    print(s, file=sys.stderr)


def count_char(maps, c):
    count = sum(line.count(c) for line in maps)
    return count
