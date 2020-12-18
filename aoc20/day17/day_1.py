import operator
import re
from typing import Dict, Tuple, Set


def neighbours(loc):
    x, y, z = loc
    neigh = []
    indexs = range(-1, 2)
    for i in indexs:
        for j in indexs:
            for k in indexs:
                neigh.append((x + i, y + j, z + k))
    neigh = neigh[0:13] + neigh[14:27]
    return neigh


all_neighbour_delta = neighbours((0, 0, 0))


def is_active(convay_cubes, loc):
    return loc in convay_cubes


def get_neighbours(loc):
    res = []
    for delta in all_neighbour_delta:
        new_loc = tuple(map(operator.add, loc, delta))
        res.append(new_loc)
    return res


def next_cycle(cur_state: Set[Tuple[int, int, int]]):
    next: Set[Tuple[int, int, int]] = set()
    calculateFor: Set[Tuple[int, int, int]] = set()
    for active_loc in cur_state:
        immediate_neighbour_arr = get_neighbours(active_loc)
        for immediate_neighbour in immediate_neighbour_arr:
            secondary_neighbour_arr = get_neighbours(immediate_neighbour)
            calculateFor = calculateFor.union(set(secondary_neighbour_arr))

    for loc in calculateFor:
        immediate_neighbour = get_neighbours(loc)
        active = [is_active(cur_state, neighbour) for neighbour in immediate_neighbour]
        active_count = sum(1 for i in active if i)
        # inactive_count = 26 - active_count
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

    convay_cubes: Set[Tuple[int, int, int]] = set()

    for i in range(0, len(inp_groups)):
        for j in range(0, len(inp_groups[i])):
            if inp_groups[i][j] == '#':
                convay_cubes.add((i, j, 0))

    state = convay_cubes
    for i in range(0, 6):
        state = next_cycle(state)

    print(len(state))


if __name__ == "__main__":
    main()
