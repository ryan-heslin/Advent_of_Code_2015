import json
import re
from collections import deque

with open("inputs/day12.txt") as f:
    raw_input = f.read()

numbers = list(map(int, (x.group(0) for x in re.finditer(r"-?\d+", raw_input))))
part1 = sum(numbers)
print(part1)

queue = json.loads(raw_input)

queue = deque([queue])

total = 0
while queue:
    this_sum = 0
    current = queue.popleft()
    is_dict = False
    if isinstance(current, dict):
        current = list(current.values())
        is_dict = True
    # Ignore current and all children
    additions = []
    for el in current:
        type_of = type(el)
        if type_of == int:
            this_sum += el
        elif type_of in (dict, list):
            additions.append(el)
        elif el == "red" and is_dict:
            # Forget everything if red found
            this_sum = 0
            additions = []
            break
    total += this_sum
    queue.extend(additions)

print(total)
