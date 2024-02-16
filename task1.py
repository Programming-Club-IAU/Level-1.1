def display_staircase(size):
    for i in range(1, size + 1):
        spaces = ' ' * (size - i)
        stars = '*' * i
        print(spaces + stars + ' ' + stars)


def main():
    size = int(input("Enter the size of the Staircase: "))
    print("Staircase:")
    display_staircase(size)


if __name__ == "__main__":
    main()
