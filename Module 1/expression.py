def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print(f"Hello {name}")
    print("4 years pass by...")
    age = age + 4
    print(f"You are {age} years old now")

if __name__ == "__main__":
    main()