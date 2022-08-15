from itertools import cycle
with open('inputs/day3.txt') as f:
    directions = f.readline().rstrip("\n")

replacements = {"^" : "0+j", "v" : "0-j", ">" : "+01", "<" : "-01" }

for k, v in replacements.items():
    directions = directions.replace(k, v)

directions =  [ complex(directions[i:(i+3)]) for i in range(0, len(directions), 3)]

visited = {complex("0")}
current = complex("0")
for coord in directions:
    current += coord
    visited.add(current)

part1 = len(visited)
print(f"Part 1: {part1}")


visited = {complex("0")}
deliverers =  [ complex("0") ] * 2
i = 0

for turn in cycle([0, 1]):
    coord = directions[i]
    deliverers[turn] += coord
    visited.add(deliverers[turn])
    i += 1
    if i == len(directions):
        break

part2 = len(visited)
print(f"Part 2: {part2}")
