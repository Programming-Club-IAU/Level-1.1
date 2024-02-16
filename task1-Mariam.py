def print_staircase(size):
    for i in range(1, size + 1):
        print('*' * i)

size = int(input("Enter the size of the Staircase: "))
print_staircase(size)