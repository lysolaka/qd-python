inp = input()

dic, search = inp.rsplit(", ", 1)

search = eval(search)
dic = eval(dic)

result = []
for k, v in dic.items():
    if v == search:
        result.append(k)

print(result)
