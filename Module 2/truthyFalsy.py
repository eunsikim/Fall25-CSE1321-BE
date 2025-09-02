def main():
    # Non-zero numeric values evaluates as `True`
    number = 10
    print(number)
    print(bool(number))

    # Zero numeric values evaluates as `False`
    number = 0
    print(number)
    print(bool(number))

    # Non-empty Sequence/Collections values evaluates as `True`
    message = "Hello World"
    print(message)
    print(bool(message))

    # Empty Sequence/Collections values evaluates as `False`
    message = ''
    print(message)
    print(bool(message))

if __name__ == "__main__":
    main()