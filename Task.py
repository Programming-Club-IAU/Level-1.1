def project(size):
    stairs = ['*' * i for i in range(1, size + 1)]
    print("\n".join(stairs))
    print('\n')
def bonus(size):
    stairs = [(" " * (size - i) + "*" * i + " " + "*" * i) for i in range(1, size + 1)]
    print("\n".join(stairs))
size_project = int(input("Please enter the size for star of the project: ")) 
project(size_project)
print ("\n--------- Mohmmad ------------- PYTHON --------- IAU --------------\n")
size_bonus = int(input("Please enter the size for star of the Bouns: "))
bonus(size_bonus)