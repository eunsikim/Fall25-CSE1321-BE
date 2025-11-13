
def main():
    try:
        # POTENTIAL ISSUE
        number = int(input("Please enter a number: "))

        print(f"You entered the number {number}")
    except ValueError:
        print("Error: program expects a numerical value")
    finally:
        print("Executing the finally block...")
    
    print("[Program Terminated]")


if __name__ == "__main__":
    main()