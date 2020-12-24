import re
from itertools import product

BIT_WIDTH = 36

mem = {}
mask = {0: 'X' * BIT_WIDTH}


# mask_and = int('1'*32, 2)
# mask_xor = int

def combinations(addr, i) -> list:
    if i == (len(addr)-1) :
        if addr[i] == 'X':
            return ['0', '1']
        return [addr[i]]

    res = combinations(addr, i + 1)
    if addr[i] == 'X':
        prefix = ['0', '1']
    else:
        prefix = [addr[i]]
    ans = product(prefix, res)
    return [k+v for(k, v) in ans]


def generate_addr(mask, addr):
    addr = list(addr)
    for (k, v) in enumerate(mask):
        if v == '1':
            addr[k] = '1'
        elif v == 'X':
            addr[k] = 'X'

    return combinations(addr, 0)


def parse_mem(inp):
    regex = re.compile(r'mem\[(\d+)\] = (\d+)')
    matches = regex.search(inp)
    addr = int(matches.group(1))
    addr = bin(addr)[2:].zfill(BIT_WIDTH)
    val = int(matches.group(2))
    address_arr = generate_addr(mask[0], addr)
    for address in address_arr:
        act_addr = int(address, 2)
        mem[act_addr] = val


def parse_mask(inp):
    regex = re.compile(r'mask = ([10X]+)')
    matches = regex.search(inp)
    mask[0] = matches.group(1)


def parse(inp: str):
    cmd = inp[0:3]
    if cmd == 'mem':
        parse_mem(inp)
    else:
        parse_mask(inp)


def main():
    f = open("input.txt", "r")
    inp = f.readline()
    while len(inp) > 0:
        parse(inp)
        inp = f.readline()

    # values_ = [int(x, 2) for x in mem.values()]
    res = sum(mem.values())
    print(res)


if __name__ == "__main__":
    main()
