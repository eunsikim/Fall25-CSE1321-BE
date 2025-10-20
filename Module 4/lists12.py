def main():
    # Join function
    states = ["Georgia", "Florida", "S. Carolina", "Alabama", "Tennessee", "N. Carolina"]

    sep = ", "

    states_str = sep.join(states)

    print(states_str)

    # Split function
    temp_str = "70,75,80,91"
    temp_list = temp_str.split(",")
    print(type(temp_list))
    print(temp_list)

if __name__ == "__main__":
    main()