def staircase (x):
    for i in range (1,x+1) :
        for t in range (x-i):
            print('  ',end='')
        for j in range (i*2):
            print ("*",end=' ')
        print()

size= int ( input ( "Enter the wanted size: " ) )
staircase(size)
