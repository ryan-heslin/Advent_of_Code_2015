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
max_hash_1 = 16**27 - 1
max_hash_2 = 16**26 - 1

part1 = find_lowest_hash(KEY, max_hash_1)
part2 = find_lowest_hash(KEY, max_hash_2)

print(part1)
print(part2)
