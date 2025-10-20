def main():
    states = ["Georgia", "Florida", "Alabama", "Tennessee", "S. Carolina", "N. Carolina"]

    for index in range(len(states)):
        print(f"{index} {states[index]}")
    
    selection = int(input("Which state do you want to change?: "))

    new_state = input("What is the state you want to change it to: ")

    states[selection] = new_state

    print()

    print(states)

if __name__ == "__main__":
    main()