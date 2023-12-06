from functools import reduce
from helpers import parse


def calc_options(total: int, button_time: int, race: [int, int]) -> int:
    time, distance = race
    return total + int((button_time * (time - button_time)) > distance)


def calc_race(total: int, race: [int, int]):
    return total * reduce(lambda x, y: calc_options(x, y, race), range(race[0]), 0)


def part_one(lines: [str]) -> int:
    times, distances = [[int(x) for x in line.split()[1:]] for line in lines]
    races = list(zip(times, distances))
    return reduce(calc_race, races, 1)


def part_two(lines: [str]) -> int:
    race = [int(''.join(line.split()[1:])) for line in lines]
    return calc_race(1, race)


if __name__ == '__main__':
    print(part_one(parse('day6/input.txt')))
    print(part_two(parse('day6/input.txt')))
