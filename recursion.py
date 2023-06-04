from typing import List

def fib(n: int) -> int:
  if n == 1:
    return 1
  if n == 2:
    return 1
  
  return fib(n-1) + fib(n-2)


def fib_memo(n: int, memo: List[int]) -> int:
  if n == 1:
    memo[n] = 1
    return memo[n]
  if n == 2:
    memo[n] = 2
    return memo[n]
  

def pow(n):
  if n == 0:
    return 1
  else:
    power = pow(n - 1)
    return power * 2
  

def factorial(n: int, memo: List[int]) -> int:
  assert n >= 0 and int(n) == n, 'Number must be positive.'

  if memo[n] > -1:
    return memo[n] 
    
  if n == 0:
    memo[n] = 1
    return memo[n]
  
  memo[n] = factorial(n - 1, memo) * n
  return memo[n]


memo = [-1] * 5000

print(factorial(5, memo))