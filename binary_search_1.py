# https://leetcode.com/problems/binary-search/


def search(self, nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    return self.search_helper(nums, left, right, target)


def search_helper(nums: list[int], left: int, right: int, target: int) -> int:
    if left > right:
        return -1
    
    middle = (left + right) // 2
    if nums[middle] == target:
        return middle
    if nums[middle] > target:
        return search_helper(nums, left, middle - 1, target)
    else:
        return search_helper(nums, middle + 1, right, target)

