def main():
    phone_battery = 100.0

    if phone_battery == 100.0:
        print("Your phone is fully charged")
        print("You should unplug the charger")

        name = input("Enter a name: ")

        number = 5 + 5

        print(f"name: {name}, number: {number}")
    else:
        print("Your phone is not fully charged")
        print("You should plug the charger")
    
    print("Program terminated")


if __name__ == "__main__":
    main()