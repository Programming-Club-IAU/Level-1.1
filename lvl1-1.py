def staircase(size):
    for i in range (1,size+1):
        print (" "*(size-i),"*"*i," ","*"*i)
size = int(input("enter the size of the staircase:"))
staircase(size)