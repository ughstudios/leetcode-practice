# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Using binary search


def peak_index_in_mountain_array(mountain: list[int]) -> int:
    left = 0
    right = len(mountain) - 1
    while left < right:
        mid = left + (right-left) // 2
        if mountain[mid] < mountain[mid+1]:
            left = mid + 1
        else:
            right = mid
    return left