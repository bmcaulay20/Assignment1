#echo.py

def echo(text: str, repetitions: int = 3) -> str:
    result = "\n".join(text[-n:] for n in range(repetitions, 0, -1))
    return result + "\n."

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
