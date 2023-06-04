from functools import wraps
import time


def memoize(function):
    memo = {}

    @wraps(function)
    def wrapper(*args):
        if args not in memo:
            memo[args] = function(*args)
        return memo[args]

    return wrapper


def print_execution_time(function):
    @wraps(function)
    def wrapper(*args):
        start_time = time.time()
        result = function(*args)
        end_time = time.time()
        print(f'{function.__name__} execution time: {end_time - start_time}')
        return result

    return wrapper
