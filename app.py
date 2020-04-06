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


print(find_indicies(nums, 10))
