def main():
    password = input("Enter password: ")

    valid = False

    # Check if the password contains at least 1 number  
    for c in password:
        if c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or c == "6" or c == "7" or c == "8" or c == "9" or c == "0":
            valid = True
            break

    # Check if password contains 8 characters or more
    count = 0
    for c in password:
        count += 1

    valid = valid and count >= 8

    if valid:
        print("Password is valid")
    else:
        print("Password is not valid")

if __name__ == "__main__":
    main()