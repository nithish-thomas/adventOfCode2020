def get_group_yes(group_ans):
    ans = set()
    for s in group_ans:
        if s=='\n':
            continue
        ans.add(s)
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
