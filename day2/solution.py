import re
from collections import defaultdict
from functools import reduce, cached_property
from operator import mul

COLOR_LIMITS = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def parse():
    with open('input.txt') as f:
        return [line.replace('\n', '') for line in f.readlines()]


class Game():
    def __init__(self, raw_line):
        self._raw_line = raw_line

    @property
    def number(self) -> int:
        for k, v in self._maxes.items():
            if v > COLOR_LIMITS[k]:
                return 0

        return int(re.search(r'\d+', self._raw_line)[0])

    @property
    def powers(self) -> int:
        return reduce(mul, [*self._maxes.values()])

    @property
    def _turns(self) -> [dict]:
        def parse_turn_string(all_turns: [dict], turn: str) -> [dict]:
            turn_details = {}
            counts = [g.strip() for g in turn.split(',')]

            for count in counts:
                color_count, color = count.split()
                turn_details[color] = int(color_count)

            return all_turns + [turn_details]

        raw_turns = self._raw_line.split(':')[1].split(';')
        return reduce(parse_turn_string, raw_turns, [])

    @cached_property
    def _maxes(self) -> dict:
        maxes = defaultdict(int)

        for turn in self._turns:
            for k, v in turn.items():
                maxes[k] = max(maxes[k], v)

        return maxes


def part_one(games: [Game]) -> int:
    return reduce(lambda x, y: x + y.number, games, 0)


def part_two(games: [Game]) -> int:
    return reduce(lambda x, y: x + y.powers, games, 0)


def build_games() -> [Game]:
    lines = parse()
    return [Game(line) for line in lines]


print(part_one(build_games()))
print(part_two(build_games()))
