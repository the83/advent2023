from helpers import parse
from day1.solution import part_one, part_two


def test_part_one():
    assert part_one(parse('tests/examples/day1example1.txt')) == 142


def test_part_two():
    assert part_two(parse('tests/examples/day1example2.txt')) == 281
