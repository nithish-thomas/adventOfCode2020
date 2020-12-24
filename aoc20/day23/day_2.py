import re
from collections import defaultdict
from typing import List, Any, Tuple, Dict, Set

MAX_CUP = 1000000


def get_input() -> List[int]:
    f = open("input2.txt", "r")
    inp = list(f.read().strip())
    inp_ = [int(val) for val in inp]
    max_val = max(inp_)
    remaining = [i for i in range(max_val+1, MAX_CUP + 1)]
    return inp_ + remaining


class Cup:
    def __init__(self, val: int):
        self.val = val
        self.next: 'Cup' = None


def print_cup(start: Cup):
    cur = start.next
    for i in range(0, 2):
        print(cur.val)
        cur = cur.next
        if cur == start:
            break


def main():
    cups_inp = get_input()
    cups = [Cup(val) for val in cups_inp]

    cups_dict = dict()
    for i, cup in enumerate(cups):
        cup.next = cups[(i + 1) % len(cups)]
        cups_dict[cup.val] = cup

    current_cup = cups[0]
    for i in range(0, 10000000):
        move(cups_dict, current_cup)
        current_cup = current_cup.next
        # if i % 100000 == 0:
        #     print(i)

    print_cup(cups_dict[1])


def move(cups_dict, current_cup):
    picked = [current_cup.next, current_cup.next.next, current_cup.next.next.next]
    current_cup.next = picked[2].next
    destination_id = current_cup.val - 1
    if destination_id <= 0:
        destination_id = MAX_CUP
    while destination_id in [pick.val for pick in picked]:
        destination_id -= 1
        if destination_id <= 0:
            destination_id = MAX_CUP
    cup_next_after_insertion = cups_dict[destination_id].next
    cups_dict[destination_id].next = picked[0]
    picked[2].next = cup_next_after_insertion


if __name__ == "__main__":
    main()
