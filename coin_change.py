# https://leetcode.com/problems/coin-change/


def coin_change(coins: list[int], amount: int) -> int:
    coins_per_amount = [amount + 1] * amount + 1
    coins_per_amount[0] = 0

    for amount in range(1, amount + 1):
        for coin in coins:
            deficit = amount - coin
            if deficit >= 0:
                coins_per_amount[amount] = min(coins_per_amount[amount], 1 + coins_per_amount[deficit])
    
    return coins_per_amount[amount] if coins_per_amount[amount] != amount + 1 else -1


assert coin_change([1, 2, 5], 11) == 3, 'Invalid solution'
