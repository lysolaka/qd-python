def print_tree(height: int):
    for i in range(height):
        for j in range(height - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        print()


height = int(input("Enter christmas tree height: "))
print_tree(height)
