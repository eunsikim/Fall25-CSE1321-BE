def main():
    for y in range(3):
        for x in range(10):
            if x == 5:
                continue
            print(x, end="")
        print()

if __name__ == "__main__":
    main()