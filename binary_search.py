import random

def binary_search(nums: list[int], num: int) -> int:
    left: int = 0
    right: int = len(nums) - 1
    mid: int = len(nums) // 2

    while nums[mid] != num:
        if nums[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2

    return mid

nums: list[int] = []

while len(nums) < 10:
    num: int = random.randint(1, 100)
    if num not in nums:
        nums.append(num)

nums.sort()

print(f'リスト: {nums}, 探索する値: {num}')
print(f'値がマッチしたインデックス: {binary_search(nums, num)}')
