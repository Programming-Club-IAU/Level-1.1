def size():
    while True:
        size = int(input("Enter the size of the staircase: "))
        if size > 0:
            return size
        else:
            ("Enter a positive number")
    
def print_single_staircase(staircase_size):
    for i in range(1, staircase_size + 1):
        print('*' * i)

def print_double_staircase(staircase_size):
    for i in range(1, staircase_size + 1):
        left_side = ' ' * (staircase_size - i) + '*' * i
        right_side = '*' * i
        print(left_side + ' ' + right_side)
    

staircase_size = size()
print("Single Sided Staircase:")
print_single_staircase(staircase_size)
print("\nDouble Sided Staircase:")
print_double_staircase(staircase_size)

    