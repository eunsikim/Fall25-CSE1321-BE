def main():
    states = ["Georgia", "Florida", "Carolina", "Alabama", "Tennessee", "Carolina"]

    print(f"We have {states.count("Carolina")} Carolinas in the list")

    print(f"The first Carolina is at index #{states.index("Carolina")}")

    print("\nLets reverse the list:")
    states.reverse()
    print(states)

    print("\nLets sort the list:")
    states.sort()
    print(states)

if __name__ == "__main__":
    main()