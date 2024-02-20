def PrintStar(size):
    for i in range(1 , size + 1 ):
        spaces= ' ' * (size - i )
        stars ='*' * i 
        print(spaces + stars + ' ' + stars)

size = int(input("Enter the size of Stars: "))

PrintStar(size)