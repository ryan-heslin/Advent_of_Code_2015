import regex

with open("inputs/day8.txt") as f:
    raw_input = f.read().splitlines()

pattern = r"([a-z])|(?:\\{2})|(\\\")|(\\x[a-f0-9]{2})"
encoding_gains = {"letters": 0, "backslash": 2, "quote": 2, "hex": 1}


def parse_string(string, pattern):
    return len(string), len(regex.findall(pattern, string))

def count_encoding(string, pattern):
    matched = regex.match(pattern, string)
    # Add 4 to escape both delimiting "" and add literal delimiting " to encoded string
    # Regular letters get no extras
    out = 4
    if matched is not None:
        out += sum(
            encoding_gains[group] * len(captures)
            for group, captures in matched.capturesdict().items()
        )
    return out

result = list(zip(*[parse_string(string, pattern) for string in raw_input]))
part1 = sum(result[0]) - sum(result[1])
print(part1)

# Net difference in characters from escaping
part2_pattern = r"^\"(?:(?P<letters>[a-z]+)|(?P<backslash>\\{2})|(?P<quote>\\\")|(?P<hex>\\x[a-f0-9]{2}))*\"$"

part2 = sum(count_encoding(string, part2_pattern) for string in raw_input)
print(part2)
