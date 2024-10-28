inp = eval(input())

out = []

[out.append(i) for i in inp if i not in out]
print(out)
