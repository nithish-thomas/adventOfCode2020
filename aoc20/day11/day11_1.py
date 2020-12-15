from typing import List


def parse_row(inp):
    return list(inp)


def next_itr(inp_arr: List[List[str]]):
    rows = len(inp_arr)
    cols = len(inp_arr[0])

    def count_seat(inp_arr, i, j, param):
        if i < 0 or i >= rows:
            return 0
        if j < 0 or j >= cols:
            return 0

        if inp_arr[i][j] == param:
            return 1
        return 0

    def next_itr_at(inp_arr: List[List[str]], i: int, j: int):
        cur_state = inp_arr[i][j]
        filled_seat = count_seat(inp_arr, i - 1, j - 1, '#') + count_seat(inp_arr, i - 1, j, '#') + count_seat(inp_arr, i - 1, j + 1, '#') \
                      + count_seat(inp_arr, i, j - 1, '#') + count_seat(inp_arr, i, j + 1, '#') \
                      + count_seat(inp_arr, i + 1, j - 1, '#') + count_seat(inp_arr, i + 1, j, '#') + count_seat(inp_arr, i + 1, j + 1, '#')
        if cur_state == 'L':
            if filled_seat == 0:
                return '#'
        elif cur_state == '#':
            if filled_seat >= 4:
                return 'L'

        return cur_state

    next_itr_state: List[List[str]] = []
    for i, row in enumerate(inp_arr):
        next_itr_state.append([])
        for j, col in enumerate(inp_arr[i]):
            next_state = next_itr_at(inp_arr, i, j)
            next_itr_state[i].append(next_state)

    return next_itr_state


def main():
    f = open("input.txt", "r")
    inp_arr = f.read().strip().split('\n')
    inp_arr: List[List[str]] = [parse_row(inp) for inp in inp_arr]

    cur_itr_state = inp_arr
    next_itr_state = next_itr(cur_itr_state)
    while cur_itr_state != next_itr_state:
        cur_itr_state = next_itr_state
        next_itr_state = next_itr(cur_itr_state)

    ans = 0
    for row in next_itr_state:
        for val in row:
            if val == '#':
                ans += 1

    print(ans)





if __name__ == "__main__":
    main()
