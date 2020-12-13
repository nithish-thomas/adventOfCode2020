import bisect


def valid(preamble: list, exp_sum):
    lo = 0
    hi = len(preamble) - 1
    while hi > lo & preamble[hi] > exp_sum:
        hi -= 1

    while hi > lo:
        sum = preamble[hi] + preamble[lo]
        if sum == exp_sum:
            return True
        elif sum <= exp_sum:
            lo += 1
        else:
            hi -= 1
    return False


def main():
    f = open("input.txt", "r")
    inp = f.read().strip().split('\n')
    inp = [int(number) for number in inp]

    preamble_len = 25
    preamble = sorted(inp[0:preamble_len])

    i = preamble_len
    while i < len(inp):
        cur = inp[i]
        is_valid = valid(preamble, cur)

        if not is_valid:
            print("Not valid")
            print(cur)
            break

        preamble.remove(inp[i-preamble_len])
        bisect.insort(preamble, cur)
        i += 1



if __name__ == "__main__":
    main()
