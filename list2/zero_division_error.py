num, den = input().split(", ", 1)

try:
    result = eval(num) / eval(den)
    print(result)
except ZeroDivisionError:
    print("Division by zero is undefined")
