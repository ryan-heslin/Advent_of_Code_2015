import math


def sum_divisors(target, max_divisor=math.inf):

    current = 3
    total = 0

    while True:
        # Algorithm from https://www.math.uh.edu/~minru/web/divis2.html#:~:text=The%20most%20basic%20method%20for,of%20positive%20divisors%20for%20n.
        # All integers divisible by 1 and themselves
        total = current + (total <= max_divisor)
        root = math.isqrt(current)
        # optimize num // 50
        for divisor in range(2, int(min(root, max_divisor)) + 1):
            divided = current / divisor
            # Only add if integer divisor; don't double-count square roots
            if divided % 1 == 0:
                total += divisor + divided
        if total >= target:
            return current
        current += 1


number = 34000000
part1_target = 34000000 // 10
part1 = sum_divisors(part1_target)
print(part1)

part2_target = math.ceil(number / 11)
part2 = sum_divisors(part2_target, 50)
print(part2)
