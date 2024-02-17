#Mohammed Natheer
for i in range(1, 5):
    print('*' * i)

#staircase code
def straicase(star1):
    for x in range(1,star1+1):
        print('*' * x)

    for y in range (star1-1, 0, -1):
        print('*' * y)
num_of_staircase = int(input("Enter the size of staircase: "))
straicase(num_of_staircase)



