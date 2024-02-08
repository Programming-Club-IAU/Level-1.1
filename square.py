#task:
def print_staircase(size):
    x=0
    while x < size:
        x=x+1
        for i in range(x):
            print("*", end =" ")
        print()
# take input from user
size = int(input("Enter the size of the staircase: "))
print("~~ here is the main program ~~")
print_staircase(size)

#bonus:
def print_staircase(size):
    x=0
    y=size
    while x < size:
        x=x+1
        for j in range(y-x):
            print(" ", end =" ") #print spaces (backward)
        for i in range(x):
            print("*", end =" ") #print stars (backward)
        print(" ", end =" ")
        for i in range(x):
            print("*", end =" ") #print start=s (forward)
        print()
# take input from user
print("~~ here is the bonus program ~~")
print_staircase(size)