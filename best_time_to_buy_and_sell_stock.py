# Problem statement
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
import sys


def max_profit(prices: list[int]) -> int:
    max_profit = 0
    min_price = sys.maxsize
    for price in prices:
        if min_price > price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


# tests
test_data = [7,1,5,3,6,4]
assert max_profit(test_data) == 5, 'Incorrect result'
