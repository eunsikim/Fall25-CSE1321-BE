def main():
    age = int(input("Enter your age: "))

    # if age >= 18:
    #     print("You are allowed to drink")
    # else:
    #     print("You are not allowed to drink yet")
    
    if age < 18:
        print("You are not allowed to drink yet")
    else:
        print("You are allowed to drink")

if __name__ == "__main__":
    main()