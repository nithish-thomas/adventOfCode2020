def countCollision(inp, right_step, down_step):
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
        i += down_step
    return collisions



def main():
    f = open("input.txt", "r")
    inp = f.read().split('\n')
    collision1 = countCollision(inp, 1 ,1)
    collision2 = countCollision(inp, 3, 1)
    collision3 = countCollision(inp, 5, 1)
    collision4 = countCollision(inp, 7, 1)
    collision5 = countCollision(inp, 1, 2)
    print(collision1)
    print(collision2)
    print(collision3)
    print(collision4)
    print(collision5)
    print(collision1 * collision2 * collision3 * collision4 * collision5)


if __name__ == '__main__':
    main()
