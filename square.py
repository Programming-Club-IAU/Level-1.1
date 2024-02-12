#python code to print stairs based on the input

#function
def print_staircase(n):
    for i in range(1, n + 1):
        stars = '*' * i
        print(stars)

#input with cheeking 
n = int(input("Enter the number of rows for the staircase: "))
if n > 0:
    print_staircase(n)
else:
    print("Please enter a positive integer.")
