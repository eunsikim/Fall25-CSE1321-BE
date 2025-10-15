def approach1():
    age1 = int(input("Enter Age 1: "))
    age2 = int(input("Enter Age 2: "))
    age3 = int(input("Enter Age 3: "))
    age4 = int(input("Enter Age 4: "))
    age5 = int(input("Enter Age 5: "))
    age6 = int(input("Enter Age 6: "))
    age7 = int(input("Enter Age 7: "))
    age8 = int(input("Enter Age 8: "))
    age9 = int(input("Enter Age 9: "))
    age10 = int(input("Enter Age 10: "))
    age11 = int(input("Enter Age 11: "))
    #...
    age40 = int(input("Enter Age 40: "))

    average = age1 + age2 + age3 + age4 + age5 + age6 + age7 + age8 + age9 + age10
    average /= 10

    print(f"The average age of Class A is {average:.2f}")

def approach2():
    average = 0

    class_size = int(input("Enter class size: "))

    for i in range(class_size):
        average += int(input(f"Enter Age {i + 1}: "))

    average /= class_size

    print(f"The average age of Class A is {average:.2f}")

def main():
    # print("Approach 1: ")
    # approach1()

    print("\nApproach 2: ")
    approach2()

if __name__ == "__main__":
    main()