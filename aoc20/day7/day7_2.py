import re
from collections import defaultdict
import functools


def parse_rule_container(rule):
    regex = re.compile(r'(.*) bags contain(.*)')
    matches = regex.match(rule)
    return matches.group(1), matches.group(2)


def parse_contained_rule(rule):
    regex = re.compile(r'((\d+) ([a-z ]+) bag)+')
    all_matches = regex.findall(rule)
    return [(lambda x: (int(x[1]), x[2]))(match) for match in all_matches]


def contains_bag(contained_bags_arr, expected_color):
    for (count, color) in contained_bags_arr:
        if color == expected_color:
            return True
    return False


def main():
    f = open("input.txt", "r")
    inp = f.read().split('\n')
    inp = list(filter(lambda inp_line: len(inp_line) != 0, inp))
    rules = [parse_rule_container(inp_line) for inp_line in inp]

    fwd_map = defaultdict(lambda: [])

    for rule in rules:
        container, contained_rule = rule
        contained_bags_arr = parse_contained_rule(contained_rule)

        fwd_map[container] = contained_bags_arr

    @functools.lru_cache
    def count_bags(color):
        bags_in_cur_color = fwd_map[color]
        if len(bags_in_cur_color) == 0:
            return 1

        ans = 0
        for (count, color) in bags_in_cur_color:
            ans += count * count_bags(color)
        return ans + 1

    print(count_bags('shiny gold')-1)



if __name__ == '__main__':
    main()
