def size():
    num = int(input("Enter the size of the staircase: "))
    return num

def printStairecase():
    staireSize = size()
    if staireSize > 0:
        for i in range(1, staireSize + 1):
            print("*" * i)
        print("Reversed staircase:")
        for i in range(1, staireSize + 1):  
            print(" " * (staireSize - i) + "*" * i, " " + "*" * i)
    else: 
        print("Enter a +ve number")

printStairecase()

