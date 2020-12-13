import bisect





def main():
    f = open("input.txt", "r")
    inp = f.read().strip().split('\n')
    inp = [int(number) for number in inp]
    invalid_num = 1721308972 # from prev question

    res = []
    sum = 0
    i = 0
    while i < len(inp):
        cur = inp[i]
        prev = sum
        sum += cur
        if prev != sum-cur:
            print("Overflow")
        res.append(cur)
        i += 1

        while (len(res) > 1) & (sum > invalid_num):
            sum -= res[0]
            res = res[1:]

        if sum == invalid_num:
            ans = min(res) + max(res)
            print(ans)
            return


if __name__ == "__main__":
    main()
