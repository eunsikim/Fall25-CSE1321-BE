def main():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    for row in board:
        for column in row:
            print(column, end="|")
        print("\n-------")
    print("\n")

    board[0][0] = "X"

    for row in board:
        for column in row:
            print(column, end="|")
        print("\n-------")
    print()
    
    board[1][1] = "O"

    for row in board:
        for column in row:
            print(column, end="|")
        print("\n-------")
    print()

    board[2][0] = "X"

    for row in board:
        for column in row:
            print(column, end="|")
        print("\n-------")
    print()

if __name__ == "__main__":
    main()