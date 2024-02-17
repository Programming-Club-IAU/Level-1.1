def Staircase(size):
    for i in range (size):
        print(" "*(size-i-1) + "*"*(i+1) + " " + "*"*(i+1))

size = int(input("Enter the size of the staircase: "))
Staircase(size)