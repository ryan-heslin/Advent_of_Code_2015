import re


def parse_string(string, pattern):
    return len(string), len(re.findall(pattern, string))


def count_encoding(string):
    # Add 4 to escape both delimiting "" and add literal delimiting " to encoded string
    # Regular letters get no extras
    out = 4
    for mtype, patt in parts.items():
        # Remove backslashes to avoid false-positive hex escape matches
        if mtype == "hex":
            new = None
            while new != string:
                new = re.sub(r"(?:\\\\)+", "", string)
                string = new
        out += len(re.findall(patt, string[1:-1:])) * encoding_gains[mtype]
    return out


with open("inputs/day8.txt") as f:
    raw_input = f.read().splitlines()

pattern = r"([a-z])|(?:\\{2})|(\\\")|(\\x[a-f0-9]{2})"
encoding_gains = {"letters": 0, "backslash": 2, "quote": 2, "hex": 1}
parts = dict(
    zip(
        encoding_gains.keys(),
        (r"[a-z]+", "(?:\\\\{2})", r"\\\"", r"(?:\\x[a-f0-9]{2})"),
    )
)


result = list(zip(*[parse_string(string, pattern) for string in raw_input]))
part1 = sum(result[0]) - sum(result[1])
print(part1)

part2 = sum(count_encoding(string) for string in raw_input)
print(part2)
