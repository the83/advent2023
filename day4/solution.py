from functools import reduce


def parse() -> [[[int], [int]]]:
    with open('input.txt') as f:
        def parse_line(line):
            return [[int(y) for y in x.split()] for x in line.split(':')[1].split('|')]

        return [parse_line(line.replace('\n', '')) for line in f.readlines()]


def count_winners(row: [[int], [int]]) -> int:
    return len(list(set(row[0]) & set(row[1])))


def part_one(data: [[[int], [int]]]) -> int:
    def calc(row):
        num_winners = count_winners(row)
        return num_winners if num_winners in [0, 1] else 2**(num_winners - 1)

    return sum([calc(row) for row in data])


def part_two(data: [[[int], [int]]]) -> int:
    def calc(total: int, idx: int) -> int:
        for i in range(count_winners(data[idx])):
            next_idx = idx + i + 1
            total = calc(total, next_idx)

        return total + 1

    return reduce(calc, range(len(data)), 0)


print(part_one(parse()))
print(part_two(parse()))
