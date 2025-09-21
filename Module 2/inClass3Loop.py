def main():
    number = int(input("Enter a number: "))

    for number in range(1, number + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=", ")
        elif number % 3 == 0:
            print("Fizz", end=", ")
        elif number % 5 == 0:
            print("Buzz", end=", ")
        else:
            print(number, end=", ")

if __name__ == "__main__":
    main()