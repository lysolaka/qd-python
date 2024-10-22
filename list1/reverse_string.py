def map_num(c: chr) -> str:
    if c.isdigit():
        return str(9 - int(c))
    else:
        return c


s = input()

for c in reversed(s):
    print(map_num(c), end="")
print()
