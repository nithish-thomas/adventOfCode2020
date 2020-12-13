import re

def parse_input(inp_str):
    reg=re.compile(r'(\d+)-(\d+) (\w): (.+)')
    group = reg.match(inp_str)
    return int(group.group(1)), int(group.group(2)), group.group(3)[0], group.group(4)

def pass_matches(password_db):
    lo, hi, ch, password = password_db
    char_lo = password[lo-1]
    char_hi = password[hi-1]
    return ((char_lo == ch) | (char_hi == ch)) & (char_lo != char_hi)

def main():
    f = open("input.txt", "r")
    inp = f.read().split('\n')
    parsed_input = [parse_input(line) for line in inp]
    print(len(parsed_input))
    matching_pass = list(filter(lambda password_db: pass_matches(password_db), parsed_input))
    print(len(matching_pass))



if __name__ == '__main__':
    main()
