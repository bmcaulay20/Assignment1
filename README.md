# Assignment1
Python Refresher
'''echo
#echo.py

def echo(text: str, repetitions: int = 3) -> str:
    result = "\n".join(text[-n:] for n in range(repetitions, 0, -1))
    return result + "\n."

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))

'''

'''fib
#fib.py

from functools import lru_cache
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"finsihed in {end_time - start_time:.6f} seconds: {func.__name__}({args[0]}) -> {result}")
        return result
    return wrapper
@lru_cache
@timer
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
def timed_fib(n):
    return fib(n)
if __name__ == "__main__":
    fib(100)
'''
