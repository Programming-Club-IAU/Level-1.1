def staircase(numb):
    for i in range(1,numb+1):
        print("*"*i)

numb = int(input("Enter the number of stairs: "))
staircase(numb)