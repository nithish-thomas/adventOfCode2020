import enum


# Using enum class create enumerations
class Direction(enum.Enum):
    North = 0
    East = 1
    South = 2
    West = 3


def left(cur_dir):
    _left = {
        Direction.North: Direction.West,
        Direction.East: Direction.North,
        Direction.South: Direction.East,
        Direction.West: Direction.South
    }
    return _left[cur_dir]


def right(cur_dir):
    _right = {
        Direction.North: Direction.East,
        Direction.East: Direction.South,
        Direction.South: Direction.West,
        Direction.West: Direction.North
    }
    return _right[cur_dir]


def main():
    f = open("input.txt", "r")
    inp_arr = f.read().strip().split('\n')

    dir_loc_delta = {
        Direction.North: (1, 0),
        Direction.East: (0, 1),
        Direction.South: (-1, 0),
        Direction.West: (0, -1)
    }

    cur_dir = Direction.East
    cur_loc = (0, 0)

    def move(cur, dir, val):
        dx, dy = dir_loc_delta[dir]
        x, y = cur
        return x + (dx * val), y + (dy * val)

    for inp in inp_arr:
        cmd = inp[0]
        val = int(inp[1:])
        if cmd == 'L':
            for t in range(0, int(val / 90)):
                cur_dir = left(cur_dir)
        elif cmd == 'R':
            for t in range(0, int(val / 90)):
                cur_dir = right(cur_dir)
        elif cmd == 'N':
            cur_loc = move(cur_loc, Direction.North, val)
        elif cmd == 'S':
            cur_loc = move(cur_loc, Direction.South, val)
        elif cmd == 'E':
            cur_loc = move(cur_loc, Direction.East, val)
        elif cmd == 'W':
            cur_loc = move(cur_loc, Direction.West, val)
        elif cmd == 'F':
            cur_loc = move(cur_loc, cur_dir, val)

    print(cur_loc)
    print(cur_dir)
    x, y = cur_loc
    print(abs(x) + abs(y))


if __name__ == "__main__":
    main()
