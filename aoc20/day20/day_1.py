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

    def get_borders(self):
        arr_len = len(self.tile)
        top_tile = self.tile[0]
        right_tile = ''.join([val[arr_len - 1] for val in self.tile])
        bottom_tile = self.tile[arr_len - 1]
        left_tile = ''.join([val[0] for val in self.tile])

        return [top_tile, right_tile, bottom_tile, left_tile]

    def rotate(self):
        self.tile = [''.join(list(i)[::-1]) for i in zip(*self.tile)]

    def flip(self):
        self.tile = [row[::-1] for row in self.tile]

    def match(self, another_tile: 'Tile'):
        borders = self.get_borders()
        other_border = another_tile.get_borders()
        for i, cur_border in enumerate(borders):
            for cur_other_border in other_border:
                if cur_border == cur_other_border:
                    return i, False
                elif cur_border == cur_other_border[::-1]:
                    return i, True


border_index_to_name = {
    0: 'top',
    1: 'right',
    2: 'bottom',
    3: 'left'
}


def main():
    f = open("input2.txt", "r")
    tiles_arr = f.read().split('\n\n')
    tiles_arr = [parse_tiles(tile) for tile in tiles_arr]
    tiles_obj_arr = [Tile(tile_id, tile) for tile_id, tile in tiles_arr]

    # fixed_tiles = [tiles_obj_arr[0]]
    # remaining_tiles = set(tiles_obj_arr[1:])
    #
    # for border, fixed_tile in enumerate(fixed_tiles):
    #     for remaining_tile in remaining_tiles:
    #         match_res = fixed_tile.match(remaining_tile)

    neighbours = defaultdict(lambda: 0)

    for i in tiles_obj_arr:
        for k in tiles_obj_arr:
            if i == k:
                continue
            borders = i.get_borders()
            other_border = k.get_borders()
            for cur_border in borders:
                for cur_other_border in other_border:
                    if cur_border == cur_other_border:
                        neighbours[i.id] += 1
                    elif cur_border == cur_other_border[::-1]:
                        neighbours[i.id] += 1

    prod = 1
    for k in neighbours:
        val = neighbours[k]
        if val != 2:
            continue
        prod *= k
        print(k)

    print(neighbours)
    print(prod)


if __name__ == "__main__":
    main()
