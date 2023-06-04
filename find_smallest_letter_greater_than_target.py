# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# https://www.youtube.com/watch?v=oOsjCIPF4rk
# Binary search problem, which is obvious because we are given a "sorted list" which we need to find something in. 
# The solution can be done in O(LogN) time



# This is an iterative solution. 
def next_greatest_letter(letters: list[str], target: str) -> str:
    low = 0
    high = len(letters)
    while low < high:
        mid = (low + high) // 2
        if letters[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return letters[low % len(letters)]
