
def main():
    f = open("input.txt", "r")
    inp_arr = f.read().strip().split(',')
    inp_arr = [int(inp) for inp in inp_arr]
    inp_arr_len = len(inp_arr)
    memory = {}

    for i, num in enumerate(inp_arr[0:-1]):
        memory[num] = i + 1

    last_num = inp_arr[-1]
    k = 0
    while k < 30000000:
        cur_turn = k + inp_arr_len + 1
        if last_num not in memory:
            nxt_num = 0
        else:
            nxt_num = (cur_turn - 1) - memory[last_num]
        if cur_turn == 30000000 or cur_turn % 10000 == 0:
            print(str(cur_turn) + ' : ' + str(nxt_num))
            if cur_turn == 30000000:
                break
        memory[last_num] = cur_turn - 1
        last_num = nxt_num
        k += 1


if __name__ == "__main__":
    main()
