import random


r_list = [random.randint(-10, 15) for _ in range(0, 10)]

with open("read_file.txt", "w") as file:
    file.write(str(r_list))

print(f"Saved random list of: {r_list}\nTo read_file.txt")

with open("read_file.txt", "r") as file:
    f_list = eval(str(file.read()))
    print(f"Read read_file.txt, found\n{f_list}")
