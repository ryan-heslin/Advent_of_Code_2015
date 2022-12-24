from math import log2
import numpy as np
with open("inputs/day17.txt") as f:
    raw_input = f.read().splitlines()

containers = [int(num) for num in raw_input]
containers.sort(reverse=True)


def find_combinations(containers, target):
    n_containers = len(containers)
    max_combinations = 2 ** (n_containers)
    found = set()
    min_length = np.inf

    for i in range(1, max_combinations + 1):
        # Trim "0b"
        num_str = bin(i)[2:]

        # Pad with 0
        num_str = ("0" * (n_containers - len(num_str))) + num_str
        # Convert to mask
        mask = np.array(list(num_str), dtype= int)
        this_combination =  containers[np.where(mask)]
        # Add combination if it sums to target
        if sum(this_combination) == target: 
            found.add(tuple(mask))
            min_length = min(len(this_combination), min_length)
    return found, min_length


combinations, min_length = find_combinations(np.array(containers), 150)
part1 = len(combinations)
print(part1)
# for i, container in containers: 
    # this_combination := [container] 
part2 = len([ combo for combo in combinations if sum(combo) == min_length ])
print(part2)

