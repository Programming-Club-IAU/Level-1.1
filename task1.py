def Project(size):
    for i in range(1, size + 1):
        print('*' * i)

def Bouns(size):
    for i in range(1, size + 1):
        print(" " * (size - i) + "*" * i + " " + "*" * i)



size = int(input("Please enter the size for star of the project: "))
Project(size)

size = int(input("Please enter the size for star of the Bouns: "))
Bouns(size)
