import re
from collections import defaultdict
from typing import List, Any, Tuple, Dict, Set

MAX_CUP = 9


def get_input() -> List[int]:
    f = open("input.txt", "r")
    inp = list(f.read().strip())
    inp_ = [int(val) for val in inp]
    return inp_


class Cup:
    def __init__(self, val: int):
        self.val = val
        self.next: 'Cup' = None


def print_cup(start: Cup):
    cur = start.next
    while True:
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
    for i in range(0, 100):
        move(cups_dict, current_cup)
        current_cup = current_cup.next

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
