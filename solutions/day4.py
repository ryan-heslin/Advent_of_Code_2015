import hashlib


def find_lowest_hash(key, max_hash):
    number = -1
    res = 16**27
    while res > max_hash:
        number += 1
        res = int(hashlib.md5(f"{key}{number}".encode("utf-8")).hexdigest(), base=16)
    return number


KEY = "yzbqklnj"
# 32 hex digits in 128 bits, at least 5 leading 0s
max_hash = 16**27 - 1


part1 = find_lowest_hash(KEY, max_hash)
part2 = find_lowest_hash(KEY, 16**26 - 1)

print(part1)
print(part2)
