from helpers import parse
from day5.solution import part_one, part_two

EXAMPLE = 'tests/examples/day5example.txt'


def test_part_one():
    assert part_one(parse(EXAMPLE)) == 35


def test_part_two():
    assert part_two(parse(EXAMPLE)) == 46
