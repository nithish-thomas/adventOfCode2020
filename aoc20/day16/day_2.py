import re
from collections import defaultdict

def parse_rules(rules):
    rules_arr = rules.split('\n')
    regex = re.compile(r'(.*): (\d+)-(\d+) (.*) (\d+)-(\d+)')
    arr_ = [(regex.match(rule)) for rule in rules_arr]
    return [(item.group(1), int(item.group(2)), int(item.group(3)), int(item.group(5)), int(item.group(6))) for item in arr_]


def matches_rule(rule, value):
    name, min_a, max_a, min_b, max_b = rule
    return (min_a <= value and value <= max_a) or (min_b <= value and value <= max_b)


def matching_rules(value, rules):
    matched_rules = [rule for rule in rules if matches_rule(rule, value)]
    return matched_rules



def validate(ticket, rules):
    values = [int(val) for val in ticket.split(',')]
    return [(value, matching_rules(value, rules)) for value in values]


def ticket_is_valid(other_ticket_arr):
    pass

def main():
    f = open("input.txt", "r")
    inp_groups = f.read().strip().split('\n\n')
    rules = parse_rules(inp_groups[0])
    my_ticket = [int(ticket) for ticket in inp_groups[1].split('\n')[1].split(',')]
    other_tickets_arr = [ticket for ticket in inp_groups[2].split('\n')[1:]]

    result_ticket_arr = [validate(ticket, rules) for ticket in other_tickets_arr]

    res = defaultdict(lambda: set(rules))
    for ticket_group_res in result_ticket_arr:
        has_no_match = [(len(matching_rules) == 0) for value, matching_rules in ticket_group_res]
        should_skip = any(has_no_match)
        if should_skip:
            continue
        for group_index, (value, matching_rules) in enumerate(ticket_group_res):
            if len(matching_rules) == 0:
                continue
            valid_rules_for_group = res[group_index]
            res[group_index] = valid_rules_for_group.intersection(matching_rules)

    all_unique = False
    fixed_group = set()
    while not all_unique:
        all_unique = True
        prev = res.copy()
        for group_index, matched_rules in prev.items():
            if len(res[group_index]) == 1:
                fixed_group = fixed_group.union(res[group_index])
            else:
                res[group_index] = res[group_index] - fixed_group
                all_unique = False

        if prev == res:
            break

    ans = 1
    for index, rules in res.items():
        rule = list(rules)[0]
        name = rule[0]
        if not name.startswith("departure"):
            continue
        ans *= my_ticket[index]

    print(ans)


if __name__ == "__main__":
    main()
