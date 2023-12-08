from helpers import parse
from day8.solution import part_one, part_two

EXAMPLE_ONE = 'tests/examples/day8example1.txt'
EXAMPLE_TWO = 'tests/examples/day8example2.txt'
EXAMPLE_THREE = 'tests/examples/day8example3.txt'


def test_part_one():
    #  assert part_one(parse(EXAMPLE_ONE)) == 2
    assert part_one(parse(EXAMPLE_TWO)) == 6


def test_part_two():
    assert part_two(parse(EXAMPLE_THREE)) == 6
