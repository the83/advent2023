import re

MAPPING = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def parse():
    with open('input.txt') as f:
        return f.readlines()


def part_one():
    data = parse()
    total = 0
    for line in data:
        digits = re.findall("\d", line)
        total += int(f"{digits[0]}{digits[-1]}")

    print(total)


def part_two():
    regexes = ['\d']
    for k, _v in MAPPING.items():
        regexes.append(k)

    regex = '(?=(' + '|'.join(regexes) + '))'
    data = parse()

    total = 0
    for line in data:
        digits = re.findall(regex, line)
        total += int(''.join([str(MAPPING.get(digits[i], digits[i])) for i in [0, -1]]))

    print(total)
