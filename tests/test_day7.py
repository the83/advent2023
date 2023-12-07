from helpers import parse
from day7.solution import part_one, part_two

EXAMPLE = 'tests/examples/day7example.txt'


def test_part_one():
    assert part_one(parse(EXAMPLE)) == 6440


def test_part_two():
    assert part_two(parse(EXAMPLE)) == 5905
