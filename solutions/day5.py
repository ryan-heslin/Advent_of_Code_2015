import re
demon_regex = r"(?=.*?(?:[aeiou]+[^aieou]*){3,})(?!.*?(?:(?:ab)|(?:cd)|(?:pq)|(?:xy))).*?([a-z])\1.*"
spawn_of_demon_regex = r"(?=.*?(?:(.).\1))(?=.*?(.{2}).*?\2).*"

with open("inputs/day5.txt") as f:
    lines = f.read().splitlines()

def count_matches(lines, pattern):
    return sum(re.match(pattern, line) is not None for line in lines)

part1 = count_matches(lines, demon_regex)
part2 = count_matches(lines, spawn_of_demon_regex)
print(part1)
print(part2)
