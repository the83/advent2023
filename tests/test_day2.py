from helpers import parse
from day2.solution import part_one, part_two

EXAMPLE = 'tests/examples/day2example.txt'


def test_part_one():
    assert part_one(parse(EXAMPLE)) == 8


def test_part_two():
    assert part_two(parse(EXAMPLE)) == 2286
