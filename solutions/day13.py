import re
from itertools import permutations

import numpy as np

signs = {"lose": -1, "gain": 1}

with open("inputs/day13.txt") as f:
    raw_input = f.read().splitlines()

output_row = 0
values = []


class Allequal:
    """Equal to everything"""

    def __eq__(self, other) -> bool:
        return True


last = Allequal()
i = 0

# Get number of people programatically
while (new := raw_input[i].split(" ")[0]) == last:
    last = new
    i += 1

# V := number of vertices
V = i + 1

values = []
# groups of 7
skip = -1

# Parse input into matrix:
# i, j := i's happiness next to j
# j, i := j's happiness next to i
# diagonal: -inf (invalid)
for person_index in range(0, len(raw_input), V - 1):
    new_vertex = [-np.inf] * V
    skip += 1
    past_skip = False
    edge_index = 0
    while edge_index < V:
        # Skip value i for row i since diagonal is invalid
        # 7 line in each group for a row of an 8-coumn matrix
        if edge_index != skip:
            matches = re.match(
                r".*(?P<sign>(?:gain|lose))\s(?P<val>\d+).*",
                raw_input[person_index + edge_index - past_skip],
            )

            new_vertex[edge_index] = signs[matches.group("sign")] * int(
                matches.group("val")
            )
        else:
            past_skip = True
        edge_index += 1
    values.append(new_vertex)

G = np.array(values)

perms = permutations(range(V))






def solve(permutations, V):
    sequence = range(V - 1)
    best = -np.inf
    for perm in permutations:
        total = 0
        for i in sequence:
            next = i + 1
            # Add edge in both directions
            total += G[perm[i]][perm[next]] + G[perm[next]][perm[i]]
        # Connect last vertext to first in both directions
        # loop unrolling is sometimes defensible
        total += G[perm[-1]][perm[0]] + G[perm[0]][perm[-1]]
        if total > best:
            best = total
            yield int(best), perm
    # return int(best)


gen = solve(perms, V)
part1 = best_perm = None
while True:
    try:
        part1, best_perm = next(gen)
    except StopIteration:
        break

print(part1)

lowest = np.inf

# Find which edge in best permutation has lowest happiness score
for i in range(V):
    next = (i + 1) % (V)
    this_happiness = G[best_perm[i]][best_perm[next]] + G[best_perm[next]][best_perm[i]]
    if this_happiness < lowest:
        lowest = this_happiness
        best_edge = (best_perm[i], best_perm[next])

# Compute happiness from inserting zero-weight vertex on it
part2 = int(part1 - lowest)
print(part2)



