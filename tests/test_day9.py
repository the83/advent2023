from helpers import parse
from day9.solution import part_one, part_two

EXAMPLE = 'tests/examples/day9example.txt'


def test_part_one():
    assert part_one(parse(EXAMPLE)) == 114


def test_part_two():
    assert part_two(parse(EXAMPLE)) == 2
