from functools import reduce


def parse() -> [str]:
    with open('input.txt') as f:
        return [line.replace('\n', '') for line in f.readlines()]


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


print(part_one(parse()))
print(part_two(parse()))
