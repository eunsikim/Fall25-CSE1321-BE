def main():
    my_list = ["Hello world", 12, 3.14, True, False, [], ()]

    print(my_list)

    my_d2_list = [
        [1, 2, 3], 
        ["Hello", "World", [True, False]]
    ]

    print(my_d2_list[1][2][1])

    my_d2_list[0][2] = 3.14

    print(my_d2_list)

    del my_d2_list[0][2]

    print(my_d2_list)

    del my_d2_list[1]

    print(my_d2_list)


if __name__ == "__main__":
    main()