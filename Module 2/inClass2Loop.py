def main():
    # The user
    USERNAME = "admin"
    PASSWORD = "password123"

    hasLoggedIn = False

    attempts = 0

    while True:
        username_input = input("Username: ")
        password_input = input("Password: ")

        if USERNAME == username_input and PASSWORD == password_input:
            print("Login Successful")
            hasLoggedIn = True
            break
        elif USERNAME != username_input and PASSWORD != password_input:
            print("Username and Password are incorrect")
        elif USERNAME != username_input: 
            print("Username incorrect")
        elif PASSWORD != password_input:
            print("Password incorrect")

        attempts += 1

        if attempts == 3:
            print("You have reached the maximum amount of attempts.")
            break
        else:
            print(f"This is attempt #{attempts}, you have {3 - attempts} attempts left")

        if not hasLoggedIn:
            print("Try again")
    
    print("Program Terminated")

if __name__ == "__main__":
    main()