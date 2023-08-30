import re
from collections import defaultdict
from itertools import permutations
from math import inf
from operator import ge


def solve(perms, comparator, start, failure, stop):
    best = start
    for perm in perms:
        distance = 0
        for i, city in enumerate(perm[:-1]):
            index = positions[city]
            distance += graph[index].neighbors.get(perm[i + 1], failure)
            # If path dead-ends, abandon it
            if distance == failure or stop(distance, best):
                break
        else:
            best = comparator(best, distance)

    return best


def parse_distances(lines):
    out = defaultdict(dict)
    # Map each parent node to a mapping of neighbors to distances
    for line in lines:
        node, neighbor, distance = re.match(
            r"^([a-zA-Z]+) to ([a-zA-Z]+) = (\d+)$", line
        ).groups()
        # Create new mapping for parent node if not yet known

        # Since edges are symmetric
        out[node][neighbor] = out[neighbor][node] = int(distance)
    return out


class Node:
    def __init__(self, name: str, neighbors: dict):
        self.name = name
        self.neighbors = neighbors

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self):
        return f"{self.name}\n{self.neighbors}"


with open("inputs/day9.txt") as f:
    raw_input = f.read().splitlines()
parsed = parse_distances(raw_input)
graph = [Node(node, neighbors) for node, neighbors in parsed.items()]
positions = {node: i for i, node in enumerate(parsed.keys())}

# Brute force works sometimes
perms = permutations(positions.keys(), len(positions.keys()))


part1 = solve(perms, min, inf, inf, ge)
perms = permutations(positions.keys(), len(positions.keys()))
part2 = solve(perms, max, -inf, -inf, lambda *_: False)
print(part1)
print(part2)
