def validate(password):
    triple = False
    doubles = 0
    # Illegal characters
    disallowed = {9, 12, 15}
    last_double = -1

    for i, num in enumerate(password):
        if num in disallowed:
            return False
        # avoid double-counting doubles
        if i > 0 and password[i] == password[i - 1] and (i - 1) != last_double:
            last_double = i
            doubles += 1

        if i > 1 and num == password[i - 1] + 1 == password[i - 2] + 2:
            triple = True
    return triple and doubles >= 2


ascii_a = 97

def increment(password):
    max_value = 26
    i = len(password) - 1

    for i in reversed(range(len(password))):
        password[i] = (password[i] + 1) % max_value 
        if password[i] != 0:
            nums2str(password)
            break


def str2nums(string):
    out = [None] * len(string)
    for i, letter in enumerate(string):
        out[i] = ord(letter) - ascii_a

    return out


def solve(password):
    while True:
        increment(password)
        if validate(password):
            yield password

def nums2str(nums):
    out = "" 
    for num in nums: 
        out += chr(num + ascii_a)
    return out

raw_input = "vzbxkghb"

parsed = str2nums(raw_input)

part1 = nums2str(next(solve(parsed)))
print(part1)

part2 = nums2str(next(solve(parsed)))
print(part2)

