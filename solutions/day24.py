from itertools import combinations
from math import inf
from math import prod

## numbers = parsed input
empty = set()


def find_best(numbers):

    best_prod = -1
    start_length = 1
    while best_prod < 0:
        starts = [set(x) for x in combinations(numbers, r=start_length)]
        starts.sort(key=prod)
        for start in starts:
            numbers.difference_update(start)
            for i in range(1, len(numbers)):
                for combo in combinations(numbers, r=i):
                    if sum(combo) == sum(start):
                        numbers.difference_update(set(combo))
                        if sum(numbers) == sum(start):
                            return prod(start)
                        numbers.update(combo)
            numbers.update(start)


def build_sequences(target, previous, remaining, groups_remaining):
    prev_sum = sum(previous)
    base_case = groups_remaining == 1
    out = False
    # target is number each combination must sum to, provided by sum of first group

    for num in remaining:
        if (new_sum := num + prev_sum) <= target:
            new_remaining = remaining - {num}
            # This group has the correct sum
            if new_sum == target:
                if base_case:
                    if not new_remaining:
                        return True
                    continue
                else:
                    # All exhausted, but not not yet in final group
                    if not new_remaining:
                        continue
                    # Recursive case: keep building
                    out = build_sequences(
                        target,
                        previous=set(),
                        remaining=new_remaining,
                        groups_remaining=groups_remaining - 1,
                    )

            # Less than case: add single number to group
            else:  
                out = build_sequences(
                    target,
                    previous=previous | {num},
                    remaining=new_remaining,
                    groups_remaining=groups_remaining,
                )
            if out:
                return True

    # Nothing found
    return False


def equal_sum_parts(numbers, target):
    partition = set()
    s = 0
    overshoots = {}

    while s != target:
        difference = target - s
        for num in numbers:
            if num <= difference and (
                min(numbers - {num}) <= difference - num <= max(numbers - {num})
            ):
                partition.add(num)
                numbers.remove(num)
                s += num


def get_arrangements(numbers, initial, n_groups):
    overall = sum(numbers)
    # starts = [set(x) for x in combinations(numbers, r = initial)]
    # starts.sort(key = prod)
    best_prod = inf
    multiplier = n_groups + 1

    for combo in combinations(numbers, r=initial):
        start = set(combo)
        # print(start)
        s = sum(start)
        if overall == multiplier * s and build_sequences(
            target=sum(start),
            previous=set(),
            remaining=numbers - start,
            groups_remaining=n_groups,
        ):
            best_prod = min(best_prod, prod(start))
    return best_prod

def solve(n_groups): 
    i = 1
    this_result = inf
    while this_result == inf:
        this_result = get_arrangements(numbers, initial=i, n_groups=n_groups)
        i += 1
    return this_result


##
##
with open("inputs/day24.txt") as f:
    raw_input = f.read().splitlines()

numbers = {int(x) for x in raw_input}



part1 = solve(n_groups = 2)
print(part1)


part2 = solve(n_groups= 3)
print(part2)

##)
