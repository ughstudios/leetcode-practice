# Leetcode # 338 https://leetcode.com/problems/counting-bits/

def count_bits(n: int) -> list[int]:
    return [bin(i).count('1') for i in range(n + 1)]


# Can use __builtin_popcount() in C++

print(count_bits(50))