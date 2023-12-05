import re
from collections import defaultdict
from functools import reduce


def parse():
    with open('input.txt') as f:
        return [line.replace('\n', '') for line in f.readlines()]


class Mapping():
    def __init__(self, name: str, raw_lines: [str]):
        self.name = name
        self._mappings = self._build(raw_lines)

    def _build(self, raw_lines: [str]) -> [[int]]:
        return [[int(x) for x in line.split(' ')] for line in raw_lines]

    def get(self, val):
        for dest, source, map_range in self._mappings:
            if val >= source and val <= source + map_range:
                num_steps = val - source
                return dest + num_steps

        return val

    def get_inverse(self, val):
        for dest, source, map_range in self._mappings:
            if val >= dest and val <= dest + map_range:
                num_steps = val - dest
                return source + num_steps

        return val


def build_mappings(lines: [str]) -> [Mapping]:
    mappings = []
    name = ''

    for idx, line in enumerate(lines):
        if re.match('\w.*map', line):
            name = line.split()[0]
            sets = []
        if re.match('^\d', line):
            sets.append(line)
        if line == '' and name != '' or idx + 1 == len(lines):
            mappings.append(Mapping(name, sets))

    return mappings


def part_one(lines: [str]) -> int:
    mappings = build_mappings(lines)
    seeds = [int(x) for x in lines[0].split(':')[1].split()]
    locations = [reduce(lambda x, y: y.get(x), mappings, seed) for seed in seeds]

    return min(locations)


def part_two(lines: [str]) -> int:
    mappings = build_mappings(lines)
    mappings.reverse()

    raw_seeds = [int(x) for x in lines[0].split(':')[1].split()]
    seed_pairs = list(zip(raw_seeds, raw_seeds[1:]))[::2]

    dest = 0

    # LOL
    while True:
        seed = reduce(lambda x, y: y.get_inverse(x), mappings, dest)

        for x, y in seed_pairs:
            if seed >= x and seed <= x + y:
                return dest

        dest += 1


print(part_one(parse()))
print(part_two(parse()))
