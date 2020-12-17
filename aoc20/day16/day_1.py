import re


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



def main():
    f = open("input.txt", "r")
    inp_groups = f.read().strip().split('\n\n')
    rules = parse_rules(inp_groups[0])
    other_tickets_arr = [ticket for ticket in inp_groups[2].split('\n')[1:]]

    sum = 0

    for ticket in other_tickets_arr:
        matched_rules_per_ticket = validate(ticket, rules)
        for value, rules_matching in matched_rules_per_ticket:
            if len(rules_matching) == 0:
                sum += int(value)

    print(sum)



if __name__ == "__main__":
    main()
