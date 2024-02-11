
"""
print('hello, World!')

for i in range(5):
    print("Hello")

def print_hello(size):
    for i in range(size):
        print("Hello")
print_hello(5)     


def print_hello(size):
    for i in range(size):
        print("Hello")
size = int(input("Enter the size of the repetetion"))
print_hello(size)
"""
def task_1(number):
    size = number

    for i in range( 1 , size + 1):
        print( "*" * i)

def task_2(number):
    size = number

    for i in range( 1 , size + 1):
        print(" " * (size - i) + "*" * i , "*" * i)


number = int(input("Enter the number of the repetetion for stair painter: "))  

task_1(number)
task_2(number)