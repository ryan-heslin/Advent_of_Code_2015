from itertools import cycle

with open("inputs/day3.txt") as f:
    directions = f.readline().rstrip("\n")

replacements = {"^": 1j, "v": -1j, ">": 1, "<": -1}

directions = [replacements[char] for char in directions]


current = 0
visited = {current}
for coord in directions:
    current += coord
    visited.add(current)

part1 = len(visited)
print(f"Part 1: {part1}")

i = 0
visited = {i}
deliverers = [i, i]

for turn in cycle((0, 1)):
    coord = directions[i]
    deliverers[turn] += coord
    visited.add(deliverers[turn])
    i += 1
    if i == len(directions):
        break

part2 = len(visited)
print(f"Part 2: {part2}")
