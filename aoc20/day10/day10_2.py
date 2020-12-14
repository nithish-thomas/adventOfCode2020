import functools
from collections import defaultdict


def solve(adapter_chain):
    chain_len = len(adapter_chain)

    @functools.lru_cache
    def possible_combinations(cur):
        if cur == chain_len - 1:
            return 1
        cur_jolt = adapter_chain[cur]
        possibilities = 0

        next_adapter = cur + 1
        while next_adapter < chain_len and adapter_chain[next_adapter] - cur_jolt <= 3:
            possibilities += possible_combinations(next_adapter)
            next_adapter += 1

        return possibilities

    return possible_combinations(0)


def main():
    f = open("input.txt", "r")
    inp = f.read().strip().split('\n')
    inp = [int(num) for num in inp]

    adapter_chain = sorted(inp)
    adapter_chain = [0] + adapter_chain + [adapter_chain[len(adapter_chain)-1]+3]

    ans = solve(adapter_chain)

    print(ans)


if __name__ == "__main__":
    main()
