def staircase(size):
    for i in range(size):
        for j in range((size-i)+1):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")

        print(" ",end="")

        for j in range(i + 1):
            print("*", end="")
        print()

size=int(input("what is size of the stair ?"))
staircase(size)