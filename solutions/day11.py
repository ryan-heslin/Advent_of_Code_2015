ASCII_A = ord("a")
DISALLOWED = {8, 11, 14}


def validate(password):
    triple = False
    doubles = 0
    last_double = -1

    for i, num in enumerate(password):
        # avoid double-counting doubles
        if i > 0 and password[i] == password[i - 1] and (i - 1) != last_double:
            last_double = i
            doubles += 1
        if i > 1 and num == password[i - 1] + 1 == password[i - 2] + 2:
            triple = True
    return triple and doubles >= 2


def increment(password):
    max_value = 26
    i = len(password) - 1

    for i in reversed(range(len(password))):
        password[i] = (password[i] + 1 + (password[i] in DISALLOWED)) % max_value
        if password[i] != 0:
            break


def str2nums(string):
    return [ord(letter) - ASCII_A for letter in string]


def solve(password):
    while True:
        increment(password)
        if validate(password):
            yield password


def nums2str(nums):
    return "".join(chr(num + ASCII_A) for num in nums)


raw_input = "vzbxkghb"
raw_input = "hepxcrrq"
parsed = str2nums(raw_input)

part1 = nums2str(next(solve(parsed)))
print(part1)

part2 = nums2str(next(solve(parsed)))
print(part2)
