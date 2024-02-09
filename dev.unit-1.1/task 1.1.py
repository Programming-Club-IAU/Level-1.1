def staircase (x):
    for i in range (1,x+1) :
        for j in range (i):
            print ("*",end='')
        print()
size= int ( input ( " Enter the wanted size " ) )
staircase(size)
