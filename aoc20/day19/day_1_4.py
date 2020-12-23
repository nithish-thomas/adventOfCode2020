import functools
import re
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
    def evaluate_rule(rule_num) -> str:
        or_rule_arr = rules[rule_num]
        if or_rule_arr == [['"a"']] or or_rule_arr == [['"b"']]:
            return '('+or_rule_arr[0][0].replace('"', '')+')'

        or_rule_eval_arr = []
        for and_rule in or_rule_arr:
            each_or_rule:List[str] = [evaluate_rule(int(rule_num)) for rule_num in and_rule]
            or_rule_eval_arr.append('('+''.join(each_or_rule)+')')

        return '('+'|'.join(or_rule_eval_arr)+')'

    return evaluate_rule(0)


def main():
    f = open("input3.txt", "r")
    inp = f.read().split('\n\n')
    rules_inp = inp[0]

    all_messages = parse_rules(rules_inp)
    print(all_messages)
    regex = re.compile(all_messages)

    messages = inp[1].split('\n')
    # fullmatch = regex.fullmatch(messages[0])
    # print(fullmatch)
    matching = [regex.fullmatch(message) for message in messages]
    valid_matches = [match for match in matching if match is not None]
    print(len(valid_matches))


if __name__ == "__main__":
    main()
