inp = eval(input())

out = []

# Alternative
# for i in inp:
#     if i not in out:
#         out.append(i)

[out.append(i) for i in inp if i not in out]
print(out)
