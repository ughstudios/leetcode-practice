# https://leetcode.com/problems/missing-number/
# https://www.youtube.com/watch?v=aaFrAFZATKU
# Sum of N natural numbers


def missing_number(nums: list[int]) -> int:
    number_of_numbers = len(nums)
    sum_of_all_numbers = sum(nums)
    sum_of_expected_numbers = number_of_numbers * (number_of_numbers + 1) // 2
    # we take the sum of N natural numbers and subtract the expected numbers from the actual amount to get the missing number
    return sum_of_expected_numbers - sum_of_all_numbers


assert missing_number([3, 0, 1]) == 2, 'Invalid result.'
