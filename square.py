size = int(input("Enter the size: "))

def stair(size):
    for i in range(size):
        for j in range(i+1):
          print("*", end="")
        print()  

stair(size)        