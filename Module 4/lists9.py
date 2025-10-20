def main():
    states = ["Georgia", "Florida", "Alabama", "Tennessee", "S. Carolina", "N. Carolina"]
    print(states)

    print()

    # Delete "Tennessee"
    del states[3]
    print(states)

    print()

    # Delete "S. Carolina" but also receive the value "S. Carolina"
    print(f"We are going to delete the state of {states.pop(3)}")
    print(states)

if __name__ == "__main__":
    main()