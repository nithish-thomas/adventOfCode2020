def get_group_yes(group_ans):
    persons_ans_arr = group_ans.split('\n')
    persons_ans_arr = list(filter(lambda x: len(x) != 0, persons_ans_arr))
    persons_ans_arr = [set(person_ans) for person_ans in persons_ans_arr]
    if len(persons_ans_arr) == 0:
        return set()
    i = 1
    ans = persons_ans_arr[0]
    while i < len(persons_ans_arr):
        ans = ans.intersection(persons_ans_arr[i])
        if len(ans) == 0:
            return ans
        i += 1
    return ans


def main():
    f = open("input.txt", "r")
    group_ans_arr = f.read().split('\n\n')
    group_ans_arr = list(filter(lambda group_ans: len(group_ans) != 0, group_ans_arr))
    group_final_ans_arr = [get_group_yes(group_ans) for group_ans in group_ans_arr]
    print('\n'.join([repr(group_final_ans) for group_final_ans in group_final_ans_arr]))
    num_yes_arr = [len(group_final_ans) for group_final_ans in group_final_ans_arr]
    print(sum(num_yes_arr))


if __name__ == '__main__':
    main()
