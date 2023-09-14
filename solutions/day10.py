from math import floor
from math import log10


class RLE:
    """Standard run length encoding"""

    def __init__(self, lengths, values):
        length = len(lengths)
        assert length == len(values)
        self.length = length

        # Confirm all runs of distinct values
        for el, lag in zip(values[1:], values[:-1]):
            assert el != lag
        self.lengths = lengths
        self.values = values

    def total_length(self):
        return sum(self.lengths)

    def __repr__(self) -> str:
        return str({"Lengths": self.lengths, "Values": self.values})

    def step(self):
        """Compute next iteration of look-see sequence"""
        new_lengths = []
        new_values = []
        last_value = Incomparable()
        for i in range(self.length):
            # Value equal to length, e.g. 22 ->
            if (val := self.values[i]) == (length := self.lengths[i]):
                these_values = [val]
                these_lengths = [2]
            # Other case: value not equal to number of repeats, e.g. 3 1s -> 3 1
            else:
                # important: length cannot equal val here
                these_values = [length, val]
                these_lengths = [1, 1]
            if last_value == these_values[0]:
                # If two digits are being added, discard only first
                new_lengths[-1] += these_lengths[0]
                these_values.pop(0)
                these_lengths.pop(0)
            new_lengths.extend(these_lengths)
            new_values.extend(these_values)
            last_value = new_values[-1]

        return new_lengths, new_values


class Incomparable:
    def __eq__(self, _):
        return False


def parse_sequence(seq):
    """Convert list of integers to lists of lengths and values, suitable for RLE creation"""
    lengths = []
    values = []
    last = Incomparable()
    for el in seq:
        if el != last:
            values.append(el)
            lengths.append(1)
            last = el
        else:
            lengths[-1] += 1

    return lengths, values


def int2list(num):
    """Convert n-digit number to n-length list"""
    return [(num // 10**i) % 10 for i in range(floor(log10(num)), -1, -1)]


raw_input = 1321131112
start_lengths, start_values = parse_sequence(int2list(raw_input))

start = RLE(start_lengths, start_values)

part1_i = 40
part2_i = 10
current = start
for __ in range(part1_i):
    current = RLE(*current.step())

part1 = current.total_length()
print(part1)

for __ in range(part2_i):
    current = RLE(*current.step())
part2 = current.total_length()
print(part2)
