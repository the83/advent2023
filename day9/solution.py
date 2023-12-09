from helpers import parse
from functools import reduce


def calc_line(total, line, is_reverse=False):
    def build_results(numbers, results):
        next_line = []
        for idx, x in enumerate(numbers):
            if idx + 1 < len(numbers):
                next_line.append(numbers[idx + 1] - x)

        results.append(next_line)

        if set(next_line) == set([0]):
            return results

        return build_results(next_line, results)

    numbers = [int(x) for x in line.split()]
    results = build_results(numbers, [numbers])
    results.reverse()

    direction, modifier = (0, -1) if is_reverse else (-1, 1)

    for idx, current_list in enumerate(results):
        if idx + 1 == len(results):
            return total + current_list[direction]

        next_number = results[idx + 1][direction] + (
            modifier * current_list[direction]
        )

        insert_idx = 0 if is_reverse else len(results[idx + 1])
        results[idx + 1].insert(insert_idx, next_number)


def part_one(lines: [str]) -> int:
    return reduce(calc_line, lines, 0)


def part_two(lines: [str]) -> int:
    return reduce(lambda x, y: calc_line(x, y, is_reverse=True), lines, 0)


if __name__ == '__main__':
    print(part_one(parse('day9/input.txt')))
    print(part_two(parse('day9/input.txt')))
