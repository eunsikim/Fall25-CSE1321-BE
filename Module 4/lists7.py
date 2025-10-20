def main():
    states = ["Georgia", "Florida", "Alabama", "Tennessee", "S. Carolina", "N. Carolina"]

    more_states = ["Texas", "Washington"]

    more_states.extend(states)

    print(more_states)

if __name__ == "__main__":
    main()