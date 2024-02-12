def staircase(n):
    for i in range(1,n+1):
        print(' '*(n-i)+'#'*(i)+' '+'#'*(i)+' '*(n-i))

Size = int(input("Enter size of the stairs: "))
staircase(Size)