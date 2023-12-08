from helpers import parse
from collections import defaultdict
import re
from numpy import lcm


def build_dataset(lines):
    instructions = [int(x) for x in list(lines.pop(0).replace('L', '0').replace('R', '1'))]

    nodes = defaultdict()

    for line in lines:
        if len(line) != 0:
            x, y, z = re.findall(r'\w{3}', line)
            nodes[x] = (y, z)

    return nodes, instructions


def part_one(lines: [str]) -> int:
    idx = 0
    nodes, instructions = build_dataset(lines)
    num_steps = 0
    node = 'AAA'

    while node != 'ZZZ':
        num_steps += 1
        direction = instructions[idx]
        node = nodes[node][direction]
        idx = 0 if idx + 1 >= len(instructions) else idx + 1

    return num_steps


def part_two(lines: [str]) -> int:
    nodes, instructions = build_dataset(lines)
    iter_nodes = [x for x in nodes.keys() if x[2] == 'A']

    cycle_lengths = []
    idx = 0
    num_turns = 0
    num_cycles = len(iter_nodes)

    while len(cycle_lengths) < num_cycles:
        num_turns += 1
        direction = instructions[idx]
        next_nodes = []

        for node in iter_nodes:
            next_node = nodes[node][direction]
            if next_node[-1] == 'Z':
                cycle_lengths.append(num_turns)
            else:
                next_nodes.append(next_node)

        idx = 0 if idx + 1 >= len(instructions) else idx + 1
        iter_nodes = next_nodes

    return lcm.reduce(cycle_lengths)


if __name__ == '__main__':
    print(part_one(parse('day8/input.txt')))
    print(part_two(parse('day8/input.txt')))
