def solution(nums):
    max_pocket = len(nums) / 2
    collections = set()

    for n in nums:
        collections.add(n)
        if len(collections) == max_pocket:
            return max_pocket
    answer = len(collections)

    return answer