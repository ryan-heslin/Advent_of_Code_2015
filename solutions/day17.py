from math import inf


def find_combinations(containers, target):
    n_containers = len(containers)
    max_combinations = 2 ** (n_containers)
    found = set()
    min_length = inf

    for i in range(1, max_combinations + 1):
        # Trim "0b"
        num_str = bin(i)[2:].zfill(n_containers)
        mask = tuple(map(int, num_str))
        this_combination = [containers[i] for i in range(n_containers) if mask[i]]

        # Pad with 0
        # Convert to mask
        # mask = np.array(list(num_str), dtype=int)
        # Add combination if it sums to target
        if sum(this_combination) == target:
            found.add(mask)
            min_length = min(len(this_combination), min_length)
    return found, min_length


with open("inputs/day17.txt") as f:
    raw_input = f.read().splitlines()

containers = list(map(int, raw_input))
containers.sort(reverse=True)


combinations, min_length = find_combinations(containers, 150)
part1 = len(combinations)
print(part1)

part2 = sum([sum(combo) == min_length for combo in combinations])
print(part2)
