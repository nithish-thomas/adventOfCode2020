import re
from collections import defaultdict
from typing import List, Any, Tuple, Dict, Set


def get_input() -> List[str]:
    f = open("input2.txt", "r")
    return f.read().strip().split('\n')


direction_delta = {
    'e': (1, -1, 0),
    'w': (-1, 1, 0),
    'se': (0, -1, 1),
    'sw': (-1, 0, 1),
    'ne': (1, 0, -1),
    'nw': (0, 1, -1)
}

def convert(direction: str) -> List[Tuple[int, int, int]]:
    i = 0
    res = []
    while i < len(direction):
        if direction[i] == 'e':
            res.append(direction_delta['e'])
            i += 1
        elif direction[i] == 'w':
            res.append(direction_delta['w'])
            i += 1
        elif direction[i:i + 2] == 'se':
            res.append(direction_delta['se'])
            i += 2
        elif direction[i:i + 2] == 'sw':
            res.append(direction_delta['sw'])
            i += 2
        elif direction[i:i + 2] == 'ne':
            res.append(direction_delta['ne'])
            i += 2
        elif direction[i:i + 2] == 'nw':
            res.append(direction_delta['nw'])
            i += 2

    return res


def get_destination(direction_arr: List[Tuple[int, int, int]], start: Tuple[int, int, int]):
    x, y, z = start
    for dx, dy, dz in direction_arr:
        x += dx
        y += dy
        z += dz

    return x, y, z


def main():
    direction_array = get_input()
    black_tiles_set: Set[Tuple[int, int, int]] = set()
    direction_tuple_array = [convert(direction) for direction in direction_array]
    destinations_arr = [get_destination(direction, (0, 0, 0)) for direction in direction_tuple_array]

    for destination_val in destinations_arr:
        if destination_val in black_tiles_set:
            black_tiles_set.remove(destination_val)
        else:
            black_tiles_set.add(destination_val)

    print(black_tiles_set)
    print(len(black_tiles_set))
    print(len(black_tiles_set)==317)


if __name__ == "__main__":
    main()
