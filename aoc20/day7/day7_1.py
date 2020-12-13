import re
from collections import defaultdict


def parse_rule_container(rule):
    regex = re.compile(r'(.*) bags contain(.*)')
    matches = regex.match(rule)
    return matches.group(1), matches.group(2)


def parse_contained_rule(rule):
    regex = re.compile(r'((\d+) ([a-z ]+) bag)+')
    all_matches = regex.findall(rule)
    return [(lambda x: (x[1], x[2]))(match) for match in all_matches]


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
    rev_map = defaultdict(lambda: [])

    for rule in rules:
        container, contained_rule = rule
        contained_bags_arr = parse_contained_rule(contained_rule)

        fwd_map[container] = contained_bags_arr
        for contained_bags in contained_bags_arr:
            contained_bags_count, contained_bags_color= contained_bags
            rev_map[contained_bags_color].append(container)

    ans = set()
    possible_container = set(rev_map['shiny gold'])
    while len(possible_container) != 0:
        for possible_bag in possible_container.copy():
            possible_container.remove(possible_bag)
            if possible_bag in ans:
                continue
            ans.add(possible_bag)
            for bag in rev_map[possible_bag]:
                possible_container.add(bag)

    print(ans)
    print(len(ans))



if __name__ == '__main__':
    main()
