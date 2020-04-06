nums = [0, 1, 2, 6, 8, 9, 10]


def find_indicies(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        # looking for complimentary number to target
        compliment = target - v
        if compliment in seen:
            # we have our set
            return [seen[compliment], i]
        seen[v] = i
    return []


def reverse(x: int) -> int:
    if x > 0:  # handle positive numbers
        a = int(str(x)[::-1])
    if x <= 0:  # handle negative numbers
        a = -1 * int(str(x*-1)[::-1])
    return a


print(find_indicies(nums, 10))
print(reverse(98457))
