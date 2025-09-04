def main():
    # Valid passwords must be 8 or more characters long.
    # Valid passwords must contain special characters: !, #
    # NEW RULE: Valid passwords must contain a number (0 - 9)
    # Output should True for valid passwords and False for invalid passwords.

    password = input("Enter password: ")

    # isValid = len(password) >= 8
    # isValid = '!' in password and '#' in password
    hasValidLength = len(password) >= 8
    hasSpecChar = '!' in password and '#' in password
    hasNumber = '1' in password or '2' in password  or '3' in password or '4' in password or '5' in password or '6' in password or '7' in password or '8' in password or '9' in password or '0' in password
    isValid = hasValidLength and hasSpecChar and hasNumber

    if isValid:
        print("Your password is valid")
    if not hasValidLength:
        print("Your password is too short (minimum 8 characters long)")
    if not hasSpecChar:
        print("Your password does not contain all special characters (!, #)")
    if not hasNumber:
        print("Your password does not contain a number")

if __name__ == "__main__":
    main()