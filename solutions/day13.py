from collections import defaultdict
from itertools import permutations
from math import inf


def parse(lines):
    signs = {"gain": 1, "lose": -1}
    result = defaultdict(lambda: 0)
    names = set()

    for line in lines:
        parts = line.split(" ")
        left = parts[0]
        right = parts[-1].rstrip(".")
        value = int(parts[3]) * signs[parts[2]]
        key = [left, right]
        key.sort()
        key = tuple(key)

        names.update(key)
        result[key] += value

    return result, names


def optimize(mapping, names):
    perms = permutations(names)
    n = len(names)
    best_happiness = -inf
    best_order = None

    for perm in perms:
        this_happiness = 0
        for i in range(n):
            key = tuple(sorted((perm[i], perm[(i + 1) % n])))
            this_happiness += mapping[key]
        if this_happiness > best_happiness:
            best_happiness = this_happiness
            best_order = perm

    return best_happiness, best_order


with open("inputs/day13.txt") as f:
    raw_input = f.read().splitlines()

mapping, names = parse(raw_input)
part1, best_order = optimize(mapping, names)
assert best_order
print(part1)
n = len(names)
lowest = min(
    mapping[tuple(sorted((best_order[i], best_order[(i + 1) % n])))] for i in range(n)
)
part2 = part1 - lowest
print(part2)
