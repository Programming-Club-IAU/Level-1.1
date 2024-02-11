#   Ahmad Alsowayan     22200000086     Level-1.1

def print_staircases(size):
    for i in range(1,size+1): #line-by-line iteration

        #printing line of staircase with left-sided hypotenuse
        for j in range(size+1 - i):
            print(' ', end=' ')
        for k in range(i):
            print('*', end=' ')
        #END

        print("|", end=' ')

        #printing line of staircase with right-sided hypotenuse
        for j in range(i):
            print('*', end=' ')
        #END

        print() #new line


print_staircases(   int(    input("please insert number of staircases: "    )   )   )