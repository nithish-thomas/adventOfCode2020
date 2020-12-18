import operator
import re
from typing import Dict, Tuple, Set, List


def neighbours(loc):
    x, y, z, w = loc
    neigh = []
    indexes = range(-1, 2)
    for i in indexes:
        for j in indexes:
            for k in indexes:
                for z in indexes:
                    neigh.append((x + i, y + j, z + k, w+z))
    neigh = neigh[0:40] + neigh[41:81]
    return neigh


all_neighbour_delta = neighbours((0, 0, 0, 0))


def is_active(convay_cubes, loc):
    return loc in convay_cubes


def get_neighbours(loc: Tuple[int, int, int, int]):
    res: List[Tuple[int, int, int, int]] = []
    for delta in all_neighbour_delta:
        new_loc = tuple(map(operator.add, loc, delta))
        res.append(new_loc)
    return res


def next_cycle(cur_state: Set[Tuple[int, int, int, int]]):
    next: Set[Tuple[int, int, int, int]] = set()
    calculate_for: Set[Tuple[int, int, int, int]] = set()
    for active_loc in cur_state:
        immediate_neighbour_arr = get_neighbours(active_loc)
        for immediate_neighbour in immediate_neighbour_arr:
            secondary_neighbour_arr = get_neighbours(immediate_neighbour)
            calculate_for = calculate_for.union(set(secondary_neighbour_arr))

    for loc in calculate_for:
        immediate_neighbour = get_neighbours(loc)
        active = [is_active(cur_state, neighbour) for neighbour in immediate_neighbour]
        active_count = sum(1 for i in active if i)
        cube_state = is_active(cur_state, loc)
        if cube_state:
            if active_count == 2 or active_count == 3:
                next.add(loc)
        else:
            if active_count == 3:
                next.add(loc)

    return next




def main():
    f = open("input.txt", "r")
    inp_groups = f.read().strip().split('\n')

    convay_cubes: Set[Tuple[int, int, int, int]] = set()

    for i in range(0, len(inp_groups)):
        for j in range(0, len(inp_groups[i])):
            if inp_groups[i][j] == '#':
                convay_cubes.add((i, j, 0, 0))

    state = convay_cubes
    for i in range(0, 6):
        state = next_cycle(state)

    print(len(state))


if __name__ == "__main__":
    main()
