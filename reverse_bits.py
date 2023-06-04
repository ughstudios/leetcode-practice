# https://leetcode.com/problems/reverse-bits/
# https://www.youtube.com/watch?v=UcoN6UjAI64
# n & 1 gets first bit


def reverse_bits(n: int) -> int:
    result = 0
    
    for i in range (32):
        bit = (n >> i) & 1
        result |= (bit << (31 - i))

    return result
