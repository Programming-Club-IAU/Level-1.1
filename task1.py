x=int(input("Enter the number of rows:"))
for i in range(x):
        print(""*(x+i)+"*"*(i+1))
print("------------")
for i in range(x):
        print(" " * (x-i) + " *" * (i+1))