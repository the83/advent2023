import re
from functools import reduce
from numpy import prod


def parse():
    with open('input.txt') as f:
        return [line.replace('\n', '') for line in f.readlines()]


def get_same_row(line: str, span, regex: str):
    left = re.search(regex + '$', line[0:span[0]])
    right = re.search('^' + regex, line[span[1]:len(line)])
    return [x[0] for x in [left, right] if x is not None]


def get_adjacent_row(line: str, span, regex: str):
    left = re.search(regex + '$', line[0:span[0]])
    right = re.search('^' + regex, line[span[1]:len(line)])
    middle = re.search(regex, line[span[0]:span[1]])

    if middle:
        matches = [x[0] for x in [left, middle, right] if x is not None]
        return [''.join(matches)]

    return [x[0] for x in [left, right] if x is not None]


def get_neighbors(lines: [str], idx: int, span, regex: str) -> str:
    indices = set([
        max(0, idx - 1),
        idx,
        min(idx + 1, len(lines) - 1)
    ])

    def find(neighbors: [str], i):
        func = get_same_row if i == idx else get_adjacent_row
        return neighbors + (func(lines[i], span, regex))

    return reduce(find, indices, [])


def get_main(lines: [str], regex: str, neighbor_regex: str, calc_func) -> [int]:
    all_matches = []
    for idx, x in enumerate(lines):
        matches = re.finditer(regex, x)
        for match in matches:
            neighbors = get_neighbors(lines, idx, match.span(), neighbor_regex)
            all_matches.append(calc_func(match[0], neighbors))

    return all_matches


def part_one(lines: [str]) -> int:
    def calc(match: str, neighbors: [str]) -> int:
        return int(match) if len(neighbors) > 0 else 0

    return sum(get_main(lines, r'\d+', r'[^\s\d\w\.]', calc))


def part_two(lines: [str]) -> int:
    def calc(_match: str, neighbors: [str]) -> int:
        return prod([int(x) for x in neighbors]) if len(neighbors) == 2 else 0

    return sum(get_main(lines, r'\*', r'\d+', calc))


print(part_one(parse()))
print(part_two(parse()))
