from math import prod
from math import inf
from itertools import combinations
## numbers = parsed input
empty = set()
def find_best(numbers): 

    best_prod = -1
    start_length = 1
    while best_prod < 0: 
        starts = [set(x) for x in combinations(numbers, r = start_length)]
        starts.sort(key = prod)
        for start in starts: 
            numbers.difference_update(start)
            for i in range(1, len(numbers)): 
                for combo in combinations(numbers, r = i): 
                    if sum(combo) == sum(start): 
                        numbers.difference_update(set(combo))
                        if sum(numbers) == sum(start):
                            return prod(start)
                        numbers.update(combo)
            numbers.update(start)

def build_sequences(target, previous, remaining):
    prev_sum = sum(previous)
    # target is number each combination must sum to, provided by sum of first group
            
    for num in remaining:
        if (new_sum := num + prev_sum ) <= target:
            new_remaining = remaining - {num}
            if new_sum == target: 
                # If first group sums to target value, all remaining numbers must sum to it as well for 
                # arrangement to be valid
                if sum(new_remaining) != target: #All numbers used
                        # No valid sum found, since numbers remain unused
                    continue
                else: # Two groups have equal sum, so valid sequence
                    #build_sequences(target, previous = set(),  remaining = new_remaining, n_groups = n_groups - 1 )
                    #confirmed.add(previous)
                    #confirmed.add(new_remaining)
                    return True
            # Sum of group being formed less than target
            else:
                out = build_sequences(target, previous | {num}, remaining = new_remaining )
                if out: 
                    return out

                # Sum still less than target
        # Sum of this group overshot

    return False
##   if (sum_reached := sum(start[-1]) == target): 
##   # Base case: found
##   if n_groups == 1: 
## *   yield new
##   else: 
##   add_to_start(new, remaining = remove new from numbers, n_groups -
##   (sum_reached))
##     
confirmed = set()



def find_arrangement(numbers, initial): 
    overall = sum(numbers)
    #starts = [set(x) for x in combinations(numbers, r = initial)]
    #starts.sort(key = prod)


    for start in combinations(numbers, r = initial): 
        start = set(start)
        candidate = numbers - start
        target = sum(numbers)
        if sum(candidate) % 2 ==0 and max(candidate) <= target:
            equal_sum_parts(numbers, target)

def equal_sum_parts(numbers, target): 
    partition = set()
    s = 0
    overshoots = {}

    while s != target:
        difference = target - s
        for num in numbers:
            if (num <= difference and (min(numbers - {num}) <= difference - num <= max(numbers - {num})) ):
                partition.add(num)
                numbers.remove(num)
                s += num
            

    


def get_arrangements(numbers, initial):
    overall = sum(numbers)
    #starts = [set(x) for x in combinations(numbers, r = initial)]
    #starts.sort(key = prod)
    best_prod = inf 

    for combo in combinations(numbers, r = initial): 
        start = set(combo)
        #print(start)
        s = sum(start)
        if overall == 3 * s  and build_sequences(target = sum(start), previous = set(), remaining = numbers - start):
            best_prod = min(best_prod, prod(start))
        # Only need to confirm at least one sequence possible, then compute product

        #try:
            #result = next(gen)
            #if result != None:
                #best_prod = min(prod(start), best_prod)
        #except StopIteration: 
            #pass
    return best_prod

            
##
##      
with open("inputs/day24.txt") as f: 
    raw_input = f.read().splitlines()

numbers = {int(x) for x in raw_input}
#part1 = find_best(numbers)
#print(part1)
##
##
i = 1 
this_result = inf
while this_result == inf: 
  this_result = get_arrangements(numbers, initial = i)
  print(i)
  i += 1

part1 = this_result 
print(part1)

##)
