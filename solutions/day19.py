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


def count_steps(mapping, molecule, values, steps=0):
    # Base case: electron found
    if molecule == "e":
        return steps
    for replacement, origin in mapping.items():
        # If molecule starts with replacement molecule, go back a step by substituting replacement origin
        matched = list(re.finditer(patterns[replacement], molecule))
        if matched:
            span = matched[0].span()
            new_molecule = molecule[: (span)[0]] + origin + molecule[(span[1]) :]
            values.add(count_steps(mapping, new_molecule, values, steps + 1))
            result = values if steps == 0 else inf
            return result
        # for matched in matches:
        #    span = matched.span()
        #    new_molecule = molecule[:(span)[0]] + origin + molecule[(span[1]):]
        # Add total steps to record of those values
        #    values.add(count_steps(mapping, new_molecule, values, steps + 1))


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

part2 = min(count_steps(inverted_map, molecule, set(), 0))
print(part2)
