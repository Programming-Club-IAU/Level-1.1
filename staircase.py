def staircase (size):
    for x in range (1, size+1):
        print (" " * (size-x) +  "*" * x + "   " + "*" * x)

size=int(input("enter the size of the staircase : "))
staircase(size)