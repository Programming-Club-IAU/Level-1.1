def Stairs(num_steps):
    print("Generating...")
    for i in range(0, num_steps):
        for j in range(0,i):
            print("*",end='')
        print("")

Stairs(int(input("Enter size : ")))