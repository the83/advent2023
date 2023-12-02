import re
from functools import reduce


def parse() -> [str]:
    with open('input.txt') as f:
        return f.readlines()


def part_one(data: [str]) -> int:
    def parse_line(total: int, line: str) -> int:
        digits = re.findall("\d", line)
        return total + int(f"{digits[0]}{digits[-1]}")

    return reduce(parse_line, data, 0)


def part_two(data: [str]) -> int:
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

    regexes = ['\d'] + [*MAPPING.keys()]
    regex = '(?=(' + '|'.join(regexes) + '))'

    def parse_line(total: int, line: str) -> int:
        digits = re.findall(regex, line)
        return total + int(''.join([str(MAPPING.get(digits[i], digits[i])) for i in [0, -1]]))

    return reduce(parse_line, data, 0)


print(part_one(parse()))
print(part_two(parse()))
