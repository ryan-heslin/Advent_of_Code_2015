from collections import Counter

with open("inputs/day1.txt") as f: 
    raw_input = f.readline().rstrip("\n")

ascii_open_paren = 40
counts = Counter(raw_input)
part1 = counts["("] - counts[")"] 
print(f"Part 1 : {part1}")

floor = 1

def first_basement(instructions): 

    floor = 0
    instructions = bytearray(instructions, "ascii")
    for position, char in enumerate(instructions): 
        floor += 1 - (char -ascii_open_paren) * 2
        if floor < 0: 
            yield position + 1


part2 = next(first_basement(raw_input))
print(f"Part 2: {part2}")



