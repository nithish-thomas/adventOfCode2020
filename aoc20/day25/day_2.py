import re
from collections import defaultdict
from typing import List, Any, Tuple, Dict, Set


def get_input() -> List[str]:
    f = open("input.txt", "r")
    return f.read().strip().split('\n')


direction_delta = {
    'e': (1, -1, 0),
    'w': (-1, 1, 0),
    'se': (0, -1, 1),
    'sw': (-1, 0, 1),
    'ne': (1, 0, -1),
    'nw': (0, 1, -1)
}


def neighbours(location: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
    x, y, z = location
    return [(x + dx, y + dy, z + dz) for dx, dy, dz in direction_delta.values()]


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


def next_day(black_tiles_curr: Set[Tuple[int, int, int]]):
    neighbour_details = [
        [(black_tile, [neighbours(neighbour)]) for neighbour in neighbours(black_tile)]
        for black_tile in black_tiles_curr
    ]
    neighbour_details = [
        [neighbours(neighbour) for neighbour in neighbours(black_tile)]
        for black_tile in black_tiles_curr
    ]

    unique_tiles = {
        neighbour
        for primary_neighbours in neighbour_details
        for secondary_neighbour in primary_neighbours
        for neighbour in secondary_neighbour
    }

    black_tiles_next: Set[Tuple[int, int, int]] = set()
    for tile in unique_tiles:
        primary_neighbours = neighbours(tile)
        black_tiles_neighbours = [neighbour for neighbour in primary_neighbours if is_black(black_tiles_curr, neighbour)]
        black_neighbours_len = len(black_tiles_neighbours)
        if is_black(black_tiles_curr, tile):
            if black_neighbours_len == 1 and black_neighbours_len == 2: #negation of the criteria
                black_tiles_next.add(tile)
        else:
            if black_neighbours_len == 2:
                black_tiles_next.add(tile)

    return black_tiles_next


def is_black(black_tiles_curr: Set[Tuple[int, int, int]], pos: Tuple[int, int, int]):
    return pos in black_tiles_curr


def main():
    direction_array = get_input()
    black_tiles_set: Set[Tuple[int, int, int]] = set()
    direction_tuple_array = [convert(direction) for direction in direction_array]
    destinations_arr = [get_destination(direction, (0, 0, 0)) for direction in direction_tuple_array]

    print(neighbours((0, 0, 0)))
    # print(neighbours((2, -2, 0)))

    for destination_val in destinations_arr:
        if destination_val in black_tiles_set:
            black_tiles_set.remove(destination_val)
        else:
            black_tiles_set.add(destination_val)

    print(black_tiles_set)
    print(len(black_tiles_set))
    # print(len(black_tiles_set) == 317)
    day2 = next_day(black_tiles_set)
    print(day2)
    print(len(day2))
    day3 = next_day(day2)
    print(day3)
    print(len(day3))


if __name__ == "__main__":
    main()
