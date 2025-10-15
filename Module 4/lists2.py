def main():
    states = ["Georgia", "Florida", "Alabama", "Tennessee", "S. Carolina", "N. Carolina"]

    for i in range(len(states)):
        if "o" in states[i]: 
            print(states[i])
    
    print()

    for p in states:
        if "o" in p:
            print(p)

if __name__ == "__main__":
    main()