number = 34000000
part1_target = 34000000 // 10
from math import floor
from math import sqrt
from math import inf
from math import ceil



def sum_divisors(target, max_divisor=inf):

    current = 3
    total = 0

    while True:
        # Algorithm from https://www.math.uh.edu/~minru/web/divis2.html#:~:text=The%20most%20basic%20method%20for,of%20positive%20divisors%20for%20n.
        # All numbers divisible by 1 and themselves
        total = current + ( total <= max_divisor )
        root = floor(sqrt(current))
        # optimize num // 50
        for divisor in range(2, min(root, max_divisor) + 1):
            divided = current / divisor
            # Only add if integer divisor; don't double-count square roots
            if divided % 1 == 0:
                total += divisor * (divided <= max_divisor)  + divided * (
                    divisor != divided
                )
        if total >= target:
            yield current
        current += 1



gen = sum_divisors(part1_target)
part1 = next(gen)
print(part1)

part2_target = ceil(number / 11)
gen = sum_divisors(part2_target, 50)
part2 = next(gen)
print(part2)
