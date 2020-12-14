from collections import defaultdict

def main():
    f = open("input.txt", "r")
    inp = f.read().strip().split('\n')
    inp = [int(num) for num in inp]

    adapter_chain = sorted(inp)
    adapter_chain = adapter_chain + [adapter_chain[len(adapter_chain)-1]+3]
    num_jolt_diff = defaultdict(lambda: 0)

    cur_jolt = 0
    for adapter_jolt in adapter_chain:
        diff = adapter_jolt - cur_jolt
        num_jolt_diff[diff] += 1
        cur_jolt = adapter_jolt

    print(num_jolt_diff[1]*num_jolt_diff[3])


if __name__ == "__main__":
    main()
