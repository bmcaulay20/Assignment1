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
![screenshot of my code and output for echo.py.](<img width="1335" height="1078" alt="Screenshot 2026-02-06 023405" src="https://github.com/user-attachments/assets/9177795a-aa77-438e-b2e5-6b3797dcbbdb" />)

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
![screenshots of my code and output for fib.py.](<img width="1209" height="935" alt="Screenshot 2026-02-06 023517" src="https://github.com/user-attachments/assets/28a6eb6c-b607-4e4a-8d69-2d355c1f2cc2" />)(<img width="262" height="293" alt="Screenshot 2026-02-06 023522" src="https://github.com/user-attachments/assets/7ec0d59f-fc74-46fd-8ea7-bfff9158df18" />)(<img width="549" height="769" alt="Screenshot 2026-02-06 023548" src="https://github.com/user-attachments/assets/f8394187-c055-4984-8e29-47765593c4d0" />)(<img width="707" height="732" alt="Screenshot 2026-02-06 023603" src="https://github.com/user-attachments/assets/ccdb40ea-7538-4436-8e77-045d3e247e0f" />)


