def main():
    ages = {
        "Alice":20, 
        "Bob":21,
        "Charlie": 22
    }

    for i in ages:
        print(f"{i} is {ages[i]} years old.")

    # If searching for a specific KEY
    print("Alice" in ages)
    
    # If searching for a specific VALUE
    print(20 in ages.values())

    # If searching for a specific KV pair
    print(("Alice", 21) in ages.items())

    # How to update a VALUE in a KV pair in the dictionary
    ages["Alice"] = 30

    if ("Alice", 20) in ages.items():
        print("We have \"Alice\" and 20 as a KV Pair")
    else:
        print("We don't have \"Alice\" and 20 as a KV Pair")

    print(ages.values())
    print(ages.items())

    # How to iterate through VALUES
    for val in ages.values():
        print(val)

    # How to iterate through KV Pairs
    for kv in ages.items():
        print(kv)

    # Addint a new KV Pair into the dictionary
    ages["David"] = 40

    for i in ages:
        print(f"{i} is {ages[i]} years old.")
    
    # Removing a KV Pair
    del ages["David"]

    for i in ages:
        print(f"{i} is {ages[i]} years old.")
    
    ages.clear()

    print(ages)


if __name__ == "__main__":
    main()