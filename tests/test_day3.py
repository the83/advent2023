from helpers import parse
from day3.solution import part_one, part_two

EXAMPLE = 'tests/examples/day3example.txt'


def test_part_one():
    assert part_one(parse(EXAMPLE)) == 4361


def test_part_two():
    assert part_two(parse(EXAMPLE)) == 467835
