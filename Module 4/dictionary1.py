def main():
    my_dictionary = {}

    ages = {
        "Alice":20, 
        "Bob":21,
        "Charlie": 22
    }

    my_numbers = {
        x: x**2 for x in range(10)
    }

    print(my_numbers)

    list_to_dictionary = dict((("a", 1), ("b", 2), ("c", 3)))

    print(list_to_dictionary)


if __name__ == "__main__":
    main()