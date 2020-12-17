import enum


# Using enum class create enumerations
import math


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


def rotate(point, angle):
    x, y = point
    s = round(math.sin(math.radians(angle)))
    c = round(math.cos(math.radians(angle)))
    return x * c - y * s, x * s + y * c


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
    way_point = (1, 10)

    def move(cur, delta, val):
        dx, dy = delta
        x, y = cur
        return x + (dx * val), y + (dy * val)

    for inp in inp_arr:
        cmd = inp[0]
        val = int(inp[1:])
        if cmd == 'L':
            way_point = rotate(way_point, -val)
        elif cmd == 'R':
            way_point = rotate(way_point, val)
        elif cmd == 'N':
            way_point = move(way_point, dir_loc_delta[Direction.North], val)
        elif cmd == 'S':
            way_point = move(way_point, dir_loc_delta[Direction.South], val)
        elif cmd == 'E':
            way_point = move(way_point, dir_loc_delta[Direction.East], val)
        elif cmd == 'W':
            way_point = move(way_point, dir_loc_delta[Direction.West], val)
        elif cmd == 'F':
            cur_loc = move(cur_loc, way_point, val)
            # way_point = (1, 10)

    print(cur_loc)
    print(cur_dir)
    x, y = cur_loc
    print(abs(x) + abs(y))


if __name__ == "__main__":
    main()
