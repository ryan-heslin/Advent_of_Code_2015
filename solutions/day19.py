import re
from collections import defaultdict
from math import inf

SPLIT_PATTERN = re.compile(r"(?<=[a-zA-Z])(?=[A-Z])")


def split_molecule(molecule):
    # Capital or lowercase followed by capital
    return re.split(
        SPLIT_PATTERN,
        molecule,
    )

def shortest(molecule, pairs, terminals):
    steps = 0
    while molecule not in terminals:
        for product, source in pairs:
            if product in molecule:
                steps += 1
                molecule = re.sub(product, source, molecule, count = 1)
    return steps + 1

with open("inputs/day19.txt") as f:
    raw_input = f.read()

replacements, molecule = raw_input.rstrip("\n").split("\n\n")
replacements = replacements.splitlines()
replacement_map = defaultdict(set)

for line in replacements:
    mol, replacement = line.split(" => ")
    # Find longest known replacement target
    replacement_map[mol].add(replacement)
longest_molecule = max(map(len, replacement_map.keys()))

inverted_map = {
    mol: key for key, replaces in replacement_map.items() for mol in replaces
}
patterns = dict(zip(inverted_map.keys(), map(re.compile, inverted_map.keys())))
found = set()
molecule_length = len(molecule)

for i in range(len(molecule)):
    # Clamp to remaining characters in molecule string
    for j in range(min(longest_molecule, molecule_length - i)):
        target = molecule[i : (i + j + 1)]
        these_replacements = replacement_map[target]
        # Only runs if replacement actually known
        for replace in these_replacements:
            found.add(molecule[:(i)] + replace + molecule[(i + j + 1) :])

part1 = len(found)
print(part1)

# Replacement : origin map

terminals = set()
for k, v in inverted_map.items():
    if v == "e": 
        terminals.add(k)

for k in terminals: 
    inverted_map.pop(k)

substitutions = sorted(inverted_map.items(), key=lambda x: len(x[0]), reverse=True)
# part2 = min(count_steps(inverted_map, molecule, set(), 0))
part2 = shortest(molecule, substitutions, 
           terminals )
print(part2)
