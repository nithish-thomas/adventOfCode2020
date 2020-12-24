import re
from collections import defaultdict

regex = re.compile(r'Tile (\d+):')


def parse_tiles(tile):
    rows = tile.split('\n')
    match = regex.match(rows[0])
    return int(match.group(1)), rows[1:]


def corners_of(v):
    arr_len = len(v)

    top = v[0]
    right = ''.join([val[arr_len - 1] for val in v])
    bottom = v[arr_len - 1]
    left = ''.join([val[0] for val in v])
    return [top, right, bottom, left]


class Tile(object):
    def __init__(self, tile_id, tile):
        self.id = tile_id
        self.tile = tile

        self.top: Tile = None
        self.right: Tile = None
        self.bottom: Tile = None
        self.left: Tile = None
        self.fixed = False

    def get_borders(self):
        arr_len = len(self.tile)
        top_tile = self.tile[0]
        right_tile = ''.join([val[arr_len - 1] for val in self.tile])
        bottom_tile = self.tile[arr_len - 1][::-1]
        left_tile = ''.join([val[0] for val in self.tile[::-1]])

        return [top_tile, right_tile, bottom_tile, left_tile]

    def rotate(self):
        if self.fixed:
            raise Exception()
        self.tile = [''.join(list(i)[::-1]) for i in zip(*self.tile)]

    def flip(self, border_id):
        if self.fixed:
            raise Exception()
        if border_id == 0 or border_id == 2:
            self.tile = [row[::-1] for row in self.tile]
        else:
            self.tile = self.tile[::-1]

    def match(self, another_tile: 'Tile'):
        borders = self.get_borders()
        other_border = another_tile.get_borders()
        for self_index, cur_border in enumerate(borders):
            for other_index, cur_other_border in enumerate(other_border):
                if cur_border == cur_other_border:
                    return self_index, other_index, False
                elif cur_border == cur_other_border[::-1]:
                    return self_index, other_index, True

    def fix(self):
        self.fixed = True


border_index_to_name = {
    0: 'top',
    1: 'right',
    2: 'bottom',
    3: 'left'
}

border_corresponding_to_neighbour = {
    0: ('bottom', 2),
    1: ('left', 3),
    2: ('top', 0),
    3: ('right', 1)
}


def main():
    f = open("input.txt", "r")
    tiles_arr = f.read().split('\n\n')
    tiles_arr = [parse_tiles(tile) for tile in tiles_arr]
    tiles_obj_arr = [Tile(tile_id, tile) for tile_id, tile in tiles_arr]

    # start = [tile for tile in tiles_obj_arr if tile.id == 1951][0]
    # start.flip(1)
    start = tiles_obj_arr[0]
    start.fix()
    to_be_worked_tiles = {start}

    remaining_tiles = set(tiles_obj_arr[1:])
    # remaining_tiles = set([tile for tile in tiles_obj_arr if tile.id != 1951])
    while len(remaining_tiles) != 0:
        fixed_tiles_copy = to_be_worked_tiles.copy()
        for fixed_tile in fixed_tiles_copy:
            for remaining_tile in remaining_tiles.copy():
                match_res = fixed_tile.match(remaining_tile)
                if match_res is not None:
                    border, matched_border, is_flipped = match_res
                    expected_border_name, expected_border = border_corresponding_to_neighbour[border]
                    steps_rotation_req = (expected_border - matched_border) % 4

                    for i in range(0, steps_rotation_req):
                        remaining_tile.rotate()
                    if is_flipped:
                        remaining_tile.flip(expected_border)

                    setattr(fixed_tile, border_index_to_name[border], remaining_tile)
                    setattr(remaining_tile, expected_border_name, fixed_tile)

                    remaining_tile.fix()
                    to_be_worked_tiles.add(remaining_tile)
            to_be_worked_tiles.remove(fixed_tile)
        remaining_tiles.difference_update(to_be_worked_tiles)

    top_left = tiles_obj_arr[0]
    while top_left.top is not None:
        top_left = top_left.top
    while top_left.left is not None:
        top_left = top_left.left

    print(repr(top_left))

    print('done')


if __name__ == "__main__":
    main()
