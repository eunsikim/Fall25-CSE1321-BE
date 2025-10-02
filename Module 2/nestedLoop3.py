def main():
    size = 5

    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
    print()

    counter = 1

    for x in range(size):
        for y in range(counter):
            print("*", end="")
        print()
        counter += 1

    print()

    # # of empty spaces
    es = size - 1
    # # of asterisks
    a = 1
    for x in range(size):
        for y in range(es):
            print(" ", end="")
        for y in range(a):
            print("*", end="")
        print()
        a += 2
        es -= 1


if __name__ == "__main__":
    main()