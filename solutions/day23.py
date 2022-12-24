import re

registers = {"a": 0.0, "b": 0.0}


def is_even(x):
    return x % 2 == 0


def inc(register, line):
    registers[register] += 1
    return line + 1


def hlf(register, line):
    registers[register] /= 2
    return line + 1


def tpl(register, line):
    registers[register] *= 3
    return line + 1


def jmp(offset, line):
    return line + offset


def jie(register, offset, line):
    return line + (offset if is_even(registers[register]) else 1)


# if one
def jio(register, offset, line):
    return line + (offset if registers[register] == 1 else 1)


with open("inputs/day23.txt") as f:
    raw_input = f.read().splitlines()

parsed_instructions = [
    re.sub(r"([a-z])(?=,)", r"'\1'",  re.sub(r"^([a-z]{3})\s([\-+a-z0-9]+)(,\s[\-+0-9]+)?$", r"\1(\2\3" + f", line={i})", line))
    for i, line in enumerate(raw_input)
]

code = [compile(source = instr, filename = "", mode = "eval") for instr in parsed_instructions]

line = 0
while 0 <= line < len(code):
    line = eval(code[line])

part1 = registers["b"]
print(part1)

registers["a"] = 1
registers["b"] = 0

line = 0
while 0 <= line < len(code):
    line = eval(code[line])

part2 = registers["b"]
print(part2)
