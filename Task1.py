def print_staircase(size): #main task function
    for i in range(1, size + 1):
        print('*' * i)

def reversed(size):
    for i in range(1 , size + 1): #bonus task
        spaces = ' ' * (size - i)  
        stars = '*' * i 
        print(spaces + stars + ' ' + stars)


def main():
    size=int(input("please enter the size of the staircase : "))
    if size>0: #check if its positive
        print("Staircase is :\n")
        print_staircase(size)
        print("reversed Staircase is :\n")
        reversed(size)
    else:
        print("please enter a positive number")
    
main()    
    