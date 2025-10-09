def main():
    # 1. Wait for the user to enter a card
    # 2. Validate/Authenticate the user
    # 3. If the user is authenticated, print the options
    # 4. Execute the appropriate option
    # 4.1 Widthrawal, Deposit, Check Balance, Exit
    # 5 Ask the user if they want to continue
    # 6.1 If the user continues, go to step 3
    # 6.2 If the user does not continue, print receipt
    # 7 Give card back
    
    while True:
        user = cardHandler()
        
        if userAuthentication(user):
            printOptions()
            option = handleOptionInput()

            if option == "1":
                withdrawal()
            elif option == "2":
                deposit()
            elif option == "3":
                getBalance()
            elif option == "4":
                printReceipt()
                returnCard()
                break



if __name__ == "__main__":
    main()