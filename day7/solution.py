from helpers import parse
from functools import reduce
from itertools import groupby, chain
from collections import defaultdict

HAND_RANKS = [
    '5',
    '41',
    '32',
    '311',
    '221',
    '2111',
    '11111',
]

def get_card_ranks(jokers=False):
    CARD_RANKS = [
        'A',
        'K',
        'Q',
        'J',
        'T',
        '9',
        '8',
        '7',
        '6',
        '5',
        '4',
        '3',
        '2',
    ]
    if not jokers:
        return CARD_RANKS
    return [x for x in CARD_RANKS if x != 'J'] + ['J']


def build_joker_hand(hand):
    card_groups = defaultdict(int)
    num_jokers = hand.count('J')

    for rank in get_card_ranks(jokers=True):
        if rank != 'J':
            card_groups[rank] += hand.count(rank)

    highest = max(card_groups, key=card_groups.get)
    card_groups[highest] += num_jokers

    return ''.join(
        sorted([str(x) for x in card_groups.values() if x > 0])
    )


def build_non_joker_hand(hand):
    return [len(''.join(h)) for _, h in groupby(sorted(list(hand)))]


def get_score_string(hand, jokers=False):
    parsed_hand = build_joker_hand(hand) if jokers else build_non_joker_hand(hand)
    return ''.join(sorted([str(x) for x in parsed_hand], reverse=True))


def get_bets(groups):
    ranked_groups = sorted(groups.items(), key=lambda k: HAND_RANKS.index(k[0]))
    bets = [[bet for _hand, bet in hands] for _hand_type, hands in ranked_groups]
    flattened = reversed(list(chain(*bets)))
    return reduce(lambda x, y: x + (y[0] + 1) * y[1], enumerate(flattened), 0)


def parse_line(line, groups, jokers=False) -> None:
    card_ranks = get_card_ranks(jokers)
    hand, bet = line.split()
    ranked_hand = [card_ranks.index(x) for x in hand]
    score_string = get_score_string(hand, jokers)
    groups[score_string] = sorted(groups[score_string] + [[ranked_hand, int(bet)]], key=lambda x: x[0])


def get_answer(lines: [str], jokers=False) -> int:
    groups = defaultdict(list)

    for line in lines:
        parse_line(line, groups, jokers=jokers)

    return get_bets(groups)


def part_one(lines: [str]) -> int:
    return get_answer(lines)


def part_two(lines: [str]) -> int:
    return get_answer(lines, jokers=True)


if __name__ == '__main__':
    print(part_one(parse('day7/input.txt')))
    print(part_two(parse('day7/input.txt')))
