def main():
    ages = []

    class_size = 10

    for i in range(class_size):
        ages.append(int(input(f"Enter Age {i + 1}: ")))

    average = 0
    for i in range(class_size):
        average += ages[i]

    average /= class_size

    print(f"The average age of Class A is {average:.2f}")
    print(ages)

if __name__ == "__main__":
    main()