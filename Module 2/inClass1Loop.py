def main():
    # The user
    USERNAME = "admin"
    PASSWORD = "password123"

    username_input = ""
    password_input = ""

    hasLoggedIn = False

    while USERNAME != username_input or PASSWORD != password_input:
        username_input = input("Username: ")
        password_input = input("Password: ")

        if USERNAME == username_input and PASSWORD == password_input:
            print("Login Successful")
            hasLoggedIn = True
        elif USERNAME != username_input and PASSWORD != password_input:
            print("Username and Password are incorrect")
        elif USERNAME != username_input: 
            print("Username incorrect")
        elif PASSWORD != password_input:
            print("Password incorrect")
        
        if not hasLoggedIn:
            print("Try again")
    

if __name__ == "__main__":
    main()