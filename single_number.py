# https://leetcode.com/problems/single-number/
from functools import reduce
from operator import xor

def single_number(nums: list[int]) -> int:
    result = nums[0]

    for num in nums[1:]:
        result ^= num

    return result


def single_number2(nums: list[int]) -> int:
    return reduce(xor, nums)


def test() -> None:
    a = 1
    b = 1
    c = 2
    d = 3
    
    #a ^= a
    a ^= b
    a ^= c
    a ^= d
    print(a)
    

test()

single_number([2,2,1]) # Returns 1