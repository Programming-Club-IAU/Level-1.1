def case(x):
    u=4
    for i in range (1,x+1):
        print("*"*i)
    print("----------")
    for i in range (1,x+1):
        print(" "*u,"*"*i,"*"*i)
        u=u-1
x=eval(input("Enter the size of the Staircase: "))
case(x)

  
    
