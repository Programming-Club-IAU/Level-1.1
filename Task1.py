def print_project_star(size):
    for i in range(1, size + 1):
        print('*' * i)
def print_bonus_star(size):
    for i in range(1, size + 1):
        print(f'{" " * (size - i)}*{"*" * (i - 1)} {"*"}{"*" * (i - 1)}')
def main():
    print("__Alimj12__--programming--club__")
    project_size = int(input("Please enter the size for the star of the project: "))
    print_project_star(project_size)
    bonus_size = int(input("Please enter the size for the star of the Bonus: "))
    print_bonus_star(bonus_size)
if __name__ == "__main__":
    main()