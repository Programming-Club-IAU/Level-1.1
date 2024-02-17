def print_stair(x):
    for i in range(1, x+1):
        stars = '*'*i
        space = (x-i) * " " 
        print(space + stars + " " + stars)

n=int(input("Enter size of the staircase: "))
print_stair(n)
