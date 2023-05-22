import re

with open("inputs/day25.txt") as f:
    raw_input = f.read()

target_row, target_column = map(int, re.findall(r"\d+", raw_input))

number = 20151125
row = column = diagonal_length = 1

while row != target_row or column != target_column:
    number *= 252533
    number %= 33554393
    if row == 1:
        row = diagonal_length + 1
        diagonal_length += 1
        column = 1
    else:
        row -= 1
        column += 1

part1 = number
print(part1)
