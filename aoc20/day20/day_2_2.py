import math
import re
from collections import defaultdict
from pprint import pprint
from typing import List, Tuple, Set

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
        bottom_tile = self.tile[arr_len - 1]
        # bottom_tile = self.tile[arr_len - 1][::-1]
        left_tile = ''.join([val[0] for val in self.tile])
        # left_tile = ''.join([val[0] for val in self.tile[::-1]])

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

    def image(self):
        return [row[1:-1] for row in self.tile[1:-1]]


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


def findMonster2(tile: List[List[str]], mnst: Tuple[int, int, Set[Tuple[int, int]]]):
    w, h, mnst_pattern = mnst
    for start_x in range(0, len(tile) - h):
        for start_y in range(0, len(tile[0]) - w):
            has_monster = True
            for mnst_x, mnst_y in mnst_pattern:
                x = mnst_x + start_x
                y = mnst_y + start_y
                if tile[x][y] != '#' and tile[x][y] != 'O':
                    has_monster = False
                    break

            if has_monster:
                print('found monster')
                for mnst_x, mnst_y in mnst_pattern:
                    x = mnst_x + start_x
                    y = mnst_y + start_y
                    tile[x][y] = 'O'


def parse_mnst():
    mnst_pattern = open("input4.txt", "r").read()
    mnst_pattern: List[str] = mnst_pattern.split('\n')
    w = len(mnst_pattern[0])
    h = len(mnst_pattern)
    mnst_pattern: List[List[str]] = [list(row) for row in mnst_pattern]
    mnst_pattern: Set[Tuple[int, int]] = {(x, y) for x in range(0, h) for y in range(0, w) if mnst_pattern[x][y] == '#'}
    return w, h, mnst_pattern


def flip(tile, type):
    if type == 0:
        return [row[::-1] for row in tile]
    else:
        return tile[::-1]


def rotate(tile):
    return [list(i)[::-1] for i in zip(*tile)]


def mark_monster(tile: List[List[str]]):
    mnst_pattern = parse_mnst()
    for i in range(0,4):
        findMonster2(tile, mnst_pattern)
        tile = flip(tile, 0)
        findMonster2(tile, mnst_pattern)
        tile = flip(tile, 0)
        tile = flip(tile, 1)
        findMonster2(tile, mnst_pattern)
        tile = flip(tile, 1)
        tile = rotate(tile)
    return tile


def place_tiles(tiles_obj_arr):
    start = tiles_obj_arr[0]
    start.fix()
    to_be_worked_tiles = {start}
    remaining_tiles = set(tiles_obj_arr[1:])
    # remaining_tiles = set([tile for tile in tiles_obj_arr if tile.id != 1951])
    while len(remaining_tiles) != 0:
        fixed_tiles_copy = to_be_worked_tiles.copy()
        for fixed_tile in fixed_tiles_copy:
            remaining_tiles_copy = remaining_tiles.copy()
            for remaining_tile in remaining_tiles_copy:
                match_res = fixed_tile.match(remaining_tile)
                if match_res is not None:
                    place_matched_tile(fixed_tile, match_res, remaining_tile)

                    remaining_tile.fix()
                    to_be_worked_tiles.add(remaining_tile)
            to_be_worked_tiles.remove(fixed_tile)
        remaining_tiles.difference_update(to_be_worked_tiles)


def place_matched_tile(fixed_tile: Tile, match_res, remaining_tile: Tile):
    border, matched_border, is_flipped = match_res
    expected_border_name, expected_border = border_corresponding_to_neighbour[border]
    steps_rotation_req = (expected_border - matched_border) % 4
    for i in range(0, steps_rotation_req):
        remaining_tile.rotate()
    is_flipped = fixed_tile.match(remaining_tile)[2]
    if is_flipped:
        remaining_tile.flip(expected_border)
    setattr(fixed_tile, border_index_to_name[border], remaining_tile)
    setattr(remaining_tile, expected_border_name, fixed_tile)


def get_top_left(tiles_obj_arr):
    top_left = tiles_obj_arr[0]
    while top_left.top is not None:
        top_left = top_left.top
    while top_left.left is not None:
        top_left = top_left.left
    return top_left


def get_image(tiles_obj_arr, top_left):
    image_with_border_len = len(top_left.tile)
    num_tiles_per_side = int(math.sqrt(len(tiles_obj_arr)))
    image_without_border_len = image_with_border_len - 2
    img_size = image_without_border_len * num_tiles_per_side
    img: List[List[str]] = [[None for x in range(img_size)] for y in range(img_size)]
    row_tile_start = top_left
    for i in range(0, num_tiles_per_side):
        start_row = i * image_without_border_len
        cur_row = row_tile_start
        for j in range(0, num_tiles_per_side):
            start_col = j * image_without_border_len
            image = cur_row.image()
            for index, row in enumerate(image):
                for col_img, char in enumerate(row):
                    img[start_row + index][start_col + col_img] = char
            cur_row = cur_row.right
        row_tile_start = row_tile_start.bottom
    # img = [''.join(row) for row in img]
    return img


def main():
    f = open("input2.txt", "r")
    tiles_arr = f.read().split('\n\n')
    tiles_arr = [parse_tiles(tile) for tile in tiles_arr]
    tiles_obj_arr = [Tile(tile_id, tile) for tile_id, tile in tiles_arr]

    # start = [tile for tile in tiles_obj_arr if tile.id == 1951][0]
    # start.flip(1)
    place_tiles(tiles_obj_arr)

    top_left = get_top_left(tiles_obj_arr)

    img = get_image(tiles_obj_arr, top_left)
    # pprint([''for row in img])
    monster = mark_monster(img)
    print_tiles(monster)

    print('don')

    count = [True for x in range(0, len(monster[0])) for y in range(0, len(monster)) if monster[x][y] == '#']
    print(len(count))


def print_tiles(img):
    pprint([' '.join(row) for row in img])


if __name__ == "__main__":
    main()
