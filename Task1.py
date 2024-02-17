def print_staircase(size):
    for row in range(1, size + 1):
        spaces = size + row
        print("" * spaces, end="")
        print("#" * row)


size = int(input("Enter the size of the Staircase: "))
print_staircase(size)
