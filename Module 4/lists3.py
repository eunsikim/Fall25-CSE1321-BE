def main():
    states = ["Georgia", "Florida", "Alabama", "Tennessee", "S. Carolina", "N. Carolina"]

    sub_list1 = states[1:4]

    print(sub_list1)

    print()

    sub_list2 = states[4:6]
    print(sub_list2)

    print()

    sub_list3 = states[::2]
    print(sub_list3)

    print()

    sub_list4 = states[1::2]
    print(sub_list4)

if __name__ == "__main__":
    main()