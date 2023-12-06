from helpers import parse
from day4.solution import part_one, part_two

EXAMPLE = 'tests/examples/day4example.txt'


def test_part_one():
    assert part_one(parse(EXAMPLE)) == 13


def test_part_two():
    assert part_two(parse(EXAMPLE)) == 30
