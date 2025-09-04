def main():
    # Valid passwords must be 8 or more characters long.
    # Valid passwords must contain special characters: !, #
    # Output should True for valid passwords and False for invalid passwords.

    password = input("Enter password: ")

    # isValid = len(password) >= 8
    # isValid = '!' in password and '#' in password
    isValid = len(password) >= 8 and '!' in password and '#' in password

    if isValid:
        print("Your password is valid")
    else:
        print("Your password is not valid")


if __name__ == "__main__":
    main()