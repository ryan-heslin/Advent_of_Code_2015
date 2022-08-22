import re

# Create dict of numbers set to 0
# Parse each line: \4 = \2 (\1, \3), subbing in bitwise symbols
# eval each line

with open("inputs/day7.txt") as f:
    raw_input = f.read().splitlines()


operators = {"NOT": "~", "OR": "|", "AND": "&", "LSHIFT": "<<", "RSHIFT": ">>"}

registers = set()


def dict_reference(key, di):
    out = key if re.match(r"\d+", key) else f"{di}['{key}']"
    return out


def parse_line(line):
    registers.update(re.findall("[a-z]+", line))
    line = re.sub(
        r"^(?P<reg1>[a-z0-9]+(?=\s))?\s?(?P<op>[A-Z]+)?\s?(?P<reg2>[a-z0-9]+)\s->\s(?P<target>[a-z]+$)",
        lambda m: f"{dict_reference(m.group('target'), 'registers')} = {dict_reference(m.group('reg1'), 'registers') if m.group('reg1') else ''} {operators.get(m.group('op'), '~~')} {dict_reference(m.group('reg2'), 'registers')}",
        line,
    )
    return line


code = [ parse_line(line) for line in raw_input]
registers = {k: None for k in registers}

# An absolutely filthy hack here to make prematurely writing to a wire trigger a ValueError:
# prepending a dummy ~~ in lines with no binary op

def run_circuit(override_value = None):
    done = [False] * len(code)
    while not all(done):
        for i, line in enumerate(code):
            try:
                if not done[i]:
                    exec(line)
                    done[i] = True
                    if override_value: 
                        registers["b"] = override_value
            except TypeError:
                pass


run_circuit()
part1 = registers["a"]
print(part1)

registers = {k: None for k in registers}
registers["b"] = part1
run_circuit(part1)
part2 = registers["a"]
print(part2)
