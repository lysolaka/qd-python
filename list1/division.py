i = input()
for n in i.split(','):
    n = n.strip()
    if all(char in "01" for char in n):
        n_ = int(n, base=2)
        if n_ % 5 == 0:
            print(f"{n}, ", end="")
    else:
        print("Invalid Input: Not a valid binary number")


print()
