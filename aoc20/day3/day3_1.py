def countCollision(inp, right_step):
    height = len(inp)
    i = 0
    cur_right = 0
    max_right = len(inp[0])
    collisions = 0
    while i < height:
        loc = inp[i][cur_right]
        if loc == '#':
            collisions += 1
        cur_right += right_step
        cur_right %= max_right
        i += 1
    return collisions



def main():
    f = open("input.txt", "r")
    inp = f.read().split('\n')
    print(countCollision(inp, 3))

if __name__ == '__main__':
    main()
