import re
from collections import defaultdict
from queue import PriorityQueue

def search(molecule, pairs, terminals):

    queue = PriorityQueue()
    queue.put((len(molecule),0,  molecule), block=False)
    current = ""
    visited = set()

    while True:
        _, steps, current = queue.get(block = False)
        if current in terminals:
            return steps + 1

        full = current
        # Greed is good!
        extra_steps = steps
        for output, input in pairs:
            if output in full:
                candidate = re.sub(output, input, full, count = 1)
                if candidate not in visited:
                    full = candidate
                    visited.add(full)
                    extra_steps += 1
                    queue.put((len(full), extra_steps , full ))



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

terminals = set()
for k, v in inverted_map.items():
    if v == "e": 
        terminals.add(k)

for k in terminals: 
    inverted_map.pop(k)

substitutions = sorted(inverted_map.items(), key=lambda x: len(x[0]), reverse=True)
part2 = search(molecule, substitutions,            terminals )
print(part2)
