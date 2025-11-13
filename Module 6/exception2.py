class NotEvenNumberError(Exception): # Inheritance, disregard this code, not something covered in CSE 1321
    def __init__(self, message = ""):
        super().__init__(message)

def main():
    evenNumbers = []

    print("[Append mode]")

    while True:
        try:
            # POTENTIAL ISSUE
            number = int(input("Enter an even number or -1 to stop: "))

            if number == -1:
                break
        
            if number % 2 == 0:
                evenNumbers.append(number)
                print("\tNumber was added into the list")
            else:
                raise NotEvenNumberError
        except ValueError:
            print("Error: Program expects numerical integer values.")
        except NotEvenNumberError:
            print("Error: Program expects an even numerical value.")
    
    print("\n[Selection Mode]")
    while True:
        try:
            for i in range(len(evenNumbers)):
                print(f"{i} -> {evenNumbers[i]}")
            
            # POTENTIAL ISSUE
            index = int(input("Enter an index or -1 to stop: "))
            
            if index == -1:
                break

            # POTENTIAL ISSUE
            print(f"You selected the number {evenNumbers[index]}")
        except ValueError:
            print("Error: Program expects a numerical integer value")
        except IndexError:
            print(f"Error: Program expects a valid index value, any values between 0 - {len(evenNumbers) - 1}")

    
    print("[Program Terminated]")


if __name__ == "__main__":
    main()