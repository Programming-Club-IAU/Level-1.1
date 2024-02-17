def staircase(S):
    for i in range(1, S + 1):
        print('*' * i)
S = int(input("Enter the size of the Staircase: "))
staircase(S)

print(" ----------------both sides of the staircase--------------\n")

def both_side(both):
 for i in range(1, both + 1):
        print(' '*(both - i)+'*' * i +' ' +'*' * i)
both = int(input("Enter the size of the Staircase: "))
both_side(both)
