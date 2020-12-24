import re
from collections import defaultdict
from typing import List, Any, Tuple, Dict, Set


def parse_food(rules):
    rules_arr = rules.split('\n')
    regex = re.compile(r'(.*)\(contains(.*)\)')
    arr_ = [(regex.match(rule)) for rule in rules_arr]
    arr_ = [(item.group(1), item.group(2)) for item in arr_]
    res: List[Tuple[List[str], List[str]]] = [(ingredients.strip().split(' '), allergens.strip().split(', ')) for ingredients, allergens in arr_]
    return res




def main():
    f = open("input2.txt", "r")
    inp_groups = f.read().strip().split('\n\n')
    foods = parse_food(inp_groups[0])

    count_ingredients_in_recipes = defaultdict(lambda: 0)


    allergen_in_ingredients: Dict[str, Set[str]] = defaultdict(lambda : set())
    for ingredients_arr, allergens_arr in foods:
        for ingredient in ingredients_arr:
            count_ingredients_in_recipes[ingredient] += 1
        for allergen in allergens_arr:
            possible_ingredients = allergen_in_ingredients[allergen]
            if len(possible_ingredients) == 0:
                possible_ingredients.update(ingredients_arr)
            else:
                possible_ingredients.intersection_update(ingredients_arr)


    while True:
        # prev = allergen_in_ingredients.copy()
        all_unique = True
        found_ingredients = set()
        for k in allergen_in_ingredients:
            ingredients_with_allergen = allergen_in_ingredients[k]
            if len(ingredients_with_allergen) == 1:
                found_ingredients.update(ingredients_with_allergen)

        for k in allergen_in_ingredients:
            ingredients_with_allergen = allergen_in_ingredients[k]
            if len(ingredients_with_allergen) > 1:
                all_unique = False
                ingredients_with_allergen.difference_update(found_ingredients)

        if all_unique:
            break

    # print(allergen_in_ingredients)

    t = allergen_in_ingredients.values()
    flat_list = [item for sublist in t for item in sublist]
    non_allergens = set(count_ingredients_in_recipes.keys()).difference(flat_list)
    ans = sum([count_ingredients_in_recipes[k] for k in non_allergens])
    print(ans)


if __name__ == "__main__":
    main()
