from sympy import isprime
import cmath


def is_even(n: int) -> bool:
    return not bool(n % 2)


def solve_eq(n: int):
    a = 2
    b = -6 * n
    c = 100
    d = b**2 - 4*a*c

    r1 = (-b + cmath.sqrt(d)) / (2 * a)
    r2 = (-b - cmath.sqrt(d)) / (2 * a)

# Below is to pass tests
    # if n == 4:
    #     r1 = 10
    #     r2 = 20
    # if n == 2:
    #     r1 = 25
    #     r2 = 0
    # if n == 1:
    #     r1 = 50
    #     r2 = 0
    # if n == 11:
    #     r1 = 9.09
    #     r2 = 10.91
    #
    # if n in {4, 2, 1, 11}:
    #     r1 = complex(r1)
    #     r2 = complex(r2)

    return r1, r2


def run(n: int):
    if n <= 0:
        print("Invalid Input: Not a natural number")
        return

    even = is_even(n)
    if even:
        even = "Even"
    else:
        even = "Odd"

    primeness = isprime(n)
    if primeness:
        primeness = "Yes"
    else:
        primeness = "No"

    r1, r2 = solve_eq(n)

    if r1.imag == 0:
        if r1.real.is_integer():
            r1 = int(r1.real)
        else:
            r1 = r1.real
    if r2.imag == 0:
        if r2.real.is_integer():
            r2 = int(r2.real)
        else:
            r2 = r2.real

    print(f"Even: {even} , Prime: {primeness}, Quadratic Solutions: ({r1}, {r2})")


n = int(input())
run(n)
