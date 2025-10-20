def main():
    states = ("Georgia", "Florida", "Carolina", "Alabama", "Tennessee", "Carolina")

    states_list = list(states) # Convert the tuple states into a list

    del states_list[0]

    states = tuple(states_list) # Convert states_list back into a tuple

    print(states)

    

if __name__ == "__main__":
    main()