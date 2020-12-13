import re


def parse_passport(inp):
    regex = re.compile(r'(\w+):([^\s]+)')
    return regex.findall(inp)


def valid_byr(value):
    byr = int(value)
    return 1920 <= byr & byr <= 2002


def valid_iyr(value):
    issue = int(value)
    return 2010 <= issue & issue <= 2020


def valid_eyr(value):
    issue = int(value)
    return 2020 <= issue & issue <= 2030


def valid_hgt(value):
    reg = re.compile(r'(\d+)(\w+)$')
    match = reg.match(value)
    num = int(match.group(1))
    if match.group(2) == 'cm':
        return 150 <= num & num <= 193
    if match.group(2) == 'in':
        return 59 <= num & num <= 76


def valid_hcl(value):
    reg = re.compile(r'#[0-9a-f]{6}$')
    match = reg.match(value)
    return match is not None


def valid_ecl(value):
    reg = re.compile(r'(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)$')
    match = reg.match(value)
    return match is not None


def valid_pid(value):
    reg = re.compile(r'\d{9}$')
    match = reg.match(value)
    return match is not None


def valid_cid(value):
    return True


passport_field_validation = {
    'byr': valid_byr,
    'iyr': valid_iyr,
    'eyr': valid_eyr,
    'hgt': valid_hgt,
    'hcl': valid_hcl,
    'ecl': valid_ecl,
    'pid': valid_pid,
    'cid': valid_cid
}


def valid(pass_data_parsed):
    if len(pass_data_parsed) < 5:
        return False
    expected = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}

    def remove(field, value):
        expected.remove(field)

    for pass_entry in pass_data_parsed:
        field, value = pass_entry
        remove(field, value)
        if not passport_field_validation[field](value):
            return False

    expected.discard("cid")
    return len(expected) == 0


def main():
    f = open("input.txt", "r")
    inp = f.read().split('\n\n')
    pass_data_parsed = [parse_passport(passport_data) for passport_data in inp]
    valid_pass = list(filter(valid, pass_data_parsed))
    print(valid_pass)
    print(len(valid_pass))


if __name__ == '__main__':
    main()
