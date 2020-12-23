import functools
from typing import Dict, List, Set



def parse_rules(rules_inp):
    rule_inp = rules_inp.split('\n')
    rules: Dict[int, List[List[str]]] = {}

    for rule in rule_inp:
        rule = rule.split(':')
        rule_sep_with_pipe = rule[1].split('|')
        rule_description: List[List[str]] = [a_rule.strip().split(" ") for a_rule in rule_sep_with_pipe]
        rules[int(rule[0])] = rule_description

    @functools.lru_cache()
    def evaluate_rule(rule_num) -> Set[str]:
        or_rule_arr = rules[rule_num]
        if or_rule_arr == [['"a"']] or or_rule_arr == [['"b"']]:
            return set(or_rule_arr[0][0].replace('"', ''))

        result = set()
        for and_rule in or_rule_arr:
            res = set()
            for rule_num in and_rule:
                string_in_rule = evaluate_rule(int(rule_num))
                if len(res) == 0:
                    res = string_in_rule
                else:
                    new_set = set()
                    for a_res in res:
                        for string in string_in_rule:
                            new_set.add(a_res+string)
                    res = new_set

            result = result.union(res)
        return result

    return evaluate_rule(0)


def main():
    f = open("input2.txt", "r")
    inp = f.read().split('\n\n')
    rules_inp = inp[0]

    all_messages = parse_rules(rules_inp)
    print(all_messages)

    messages = inp[1].split('\n')
    valid_message = [message for message in messages if message in all_messages]
    print(len(valid_message))


if __name__ == "__main__":
    main()
