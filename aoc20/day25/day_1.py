import functools
import re
from collections import defaultdict
from typing import List, Any, Tuple, Dict, Set


def get_input() -> List[int]:
    f = open("input.txt", "r")
    split = f.read().strip().split('\n')
    inp = [int(val) for val in split]
    return inp


@functools.lru_cache()
def convert_subject_number(loop: int):
    if loop == 1:
        return 7 % 20201227
    val = convert_subject_number(loop - 1)
    val *= 7
    val %= 20201227
    return val


def convert_subject_number2(sub_num: int, loop: int):
    val = 1
    for i in range(0, loop):
        val *= sub_num
        val %= 20201227
    return val


# attack

def main():
    # public_keys = get_input()

    public_key_to_loop = dict()
    for i in range(1, 20201228):
        public_key = convert_subject_number(i)
        if public_key not in public_key_to_loop:
            public_key_to_loop[public_key] = i
    # public_key_to_loop = {convert_subject_number(i): i for i in range(1, 20201228)}

    get_encryption(5764801, 17807724, public_key_to_loop)
    get_encryption(2959251, 4542595, public_key_to_loop)

    # print(public_key_to_loop[2959251])
    # print(public_key_to_loop[4542595])


def get_encryption(card_pub, door_pub, public_key_to_loop):
    print("vals")
    card_loop = public_key_to_loop[card_pub]
    print(card_loop)
    door_loop = public_key_to_loop[door_pub]
    print(door_loop)
    print("encryption")
    print(convert_subject_number2(door_pub, card_loop))
    print(convert_subject_number2(card_pub, door_loop))
    print("")
    print("")


if __name__ == "__main__":
    main()
