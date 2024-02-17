def print_staircase(size):
    for i in range(1, size + 1):
        print('*' * i)
size = int(input("Enter the staircase size: "))
print_staircase(size)