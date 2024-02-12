def print_staircase(size):
    for i in range(1, size + 1):
        print(" " * (size - i), end="")
        print("*" * i, end="")
        print(" " * 2, end="")
        print("*" * i)
size = int(input("Enter the size of the Staircase: "))
print_staircase(size)