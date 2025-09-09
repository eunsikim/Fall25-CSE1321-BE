def main():
    # The user
    USERNAME = "admin"
    PASSWORD = "password123"

    username_input = input("Username: ")
    password_input = input("Password: ")

    if USERNAME == username_input and PASSWORD == password_input:
        print("Login Successful")
    elif USERNAME != username_input and PASSWORD != password_input:
        print("Username and Password are incorrect")
    elif USERNAME != username_input: 
        print("Username incorrect")
    elif PASSWORD != password_input:
        print("Password incorrect")
    

if __name__ == "__main__":
    main()