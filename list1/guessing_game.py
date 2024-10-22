import random


def guess_number(n: int) -> bool:
    if n == random.randint(1, 9):
        print("Well guessed!")
        return True
    else:
        return False
