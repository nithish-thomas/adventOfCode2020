from typing import List, Dict, Tuple


def parse_rules(rules_inp):
    rule_inp = rules_inp.split('\n')
    rules: Dict[int, List[List[str]]] = {}

    for rule in rule_inp:
        rule = rule.split(':')
        rule_sep_with_pipe = rule[1].split('|')
        rule_description: List[List[str]] = [a_rule.strip().split(" ") for a_rule in rule_sep_with_pipe]
        rules[int(rule[0])] = rule_description

    return rules


# class Rule:
#     def __init__(self):
#         self.or_rules: List[List[Rule]] = []
#         self.end =False
#         self.char = None
#
#     def match(self, string: str, start: int) -> List[Tuple[bool, int]]:
#         if self.char is not None:
#             if string[start] ==self.char:
#                 return [(True, start + 1)]
#             else:
#                 return []
#
#         res: List[Tuple[bool, int]] =[]
#         for each_rule in self.or_rules:
#             for sub_rule in each_rule:
#                 sub_rule.match()



class PrefixNode:
    def __init__(self):
        self.val: Dict[str, PrefixNode] = {}
        self.end = False

    def add_val(self, val):
        if val not in self.val:
            self.val[val] = PrefixNode()
        return self.val[val]

    def get_val(self, val):
        return self.val[val]

    def set_end(self):
        self.end = True

    def clone(self):



end_node = PrefixNode()

rules_cache = {}


def evaluate_rules(rules: Dict[int, List[List[str]]], number):
    if number in rules_cache:
        return rules_cache[number]

    rule = rules[number]
    if rule == [['"a"']] or rule == [[''"b"'']]:
        val = rule[0][0].replace('"', '')
        return PrefixNode().add_val(val)
    else:

        for each_or_rule in rule:
            for rule_id in each_or_rule:
                rule_id = evaluate_rules(rule_id)
        return


def main():
    f = open("input.txt", "r")
    inp = f.read().split('\n\n')
    rules_inp = inp[0]

    rules = parse_rules(rules_inp)
    print(rules)
    prefix_tree = evaluate_rules(rules)


if __name__ == "__main__":
    main()
