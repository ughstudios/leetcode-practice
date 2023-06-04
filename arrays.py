from array import *
from typing import List

test_cases = [
    [9], # [1, 0]
    [1,9,0], # [1, 9, 1]
    [0], # [1],
    [9, 9] # [1, 0, 0]
]

#arr = array('i', [1,2,3,4,5])
#print(arr.count(3))

"""
def plusOne(digits: List[int]) -> List[int]:
    output_digits = []
    if digits[-1] == 9:
        output_digits.insert(len(digits) - 1, 1)
        output_digits.append(0)
    else:
        output_digits.extend(digits)
        output_digits[-1] += 1
    return output_digits

for test_case in test_cases:
    output = plusOne(test_case)
    print(output)
"""


import numpy as np

twoDArray = np.array([[1,2,3], [4, 5, 6]])

# Axis, 1 = column, 0 = row
twoDArray = np.append(twoDArray, [[4,9,2]], 0)
#print(twoDArray)

new_arr = np.delete(twoDArray, 0, 0)
#print(new_arr)

#for arr in twoDArray:
    #for num in arr:
        #print(num)



mylist = [1,2,3,4,5]
del mylist[0:2]
#print(mylist)

#myarr = np.array([1,2,3,4,5])
#print(myarr / 2)


#a = [1,2,3,4,5,6,7,8,9]
#print(a[::2])


# https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
# sum of n series equation
def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    sum1 = n*(n+1)//2
    sum2 = sum(nums)
    return sum1 - sum2


test_data = [0,0,1,1,1,2,2,3,3,4]

def remove_duplicates(nums: list[int]) -> int:
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

remove_duplicates(test_data)
    


