def is_even(n: int) -> bool:
    """
    Returns True, when n is even, false otherwise.
    """
    if n % 2 == 0:
        return True
    else:
        return False


n = int(input("N: "))
print(is_even(n))
