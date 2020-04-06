nums = [0, 1, 2, 6, 8, 9, 10]


def find_indicies(nums, target):
    seenit = set()
    seen = {}
    for i, v in enumerate(nums):
        remaining = target - v
        if remaining in seen:
            return [seen[remaining], i]
        seen[v] = i
        seenit.add(i)
    return []


def reverse(x: int) -> int:
    if x > 0:  # handle positive numbers
        a = int(str(x)[::-1])
    if x <= 0:  # handle negative numbers
        a = -1 * int(str(x*-1)[::-1])
    min = -2**31
    max = 2**31 - 1
    if a not in range(min, max):
        return 0
    else:
        return a


print(find_indicies(nums, 10))
print(reverse(98457))
